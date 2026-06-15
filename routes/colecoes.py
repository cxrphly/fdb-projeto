from flask import Blueprint, render_template, request, redirect, url_for, flash
from database import db
from models import Colecao, MaterialDidatico, Usuario, material_colecao

colecoes_bp = Blueprint("colecoes", __name__)


@colecoes_bp.route("/")
def listar():
    q = request.args.get("q", "")

    query = Colecao.query.filter_by(ativa=True)
    if q:
        query = query.filter(Colecao.nome.ilike(f"%{q}%"))

    colecoes = query.order_by(Colecao.data_criacao.desc()).all()
    return render_template("colecoes/listar.html", colecoes=colecoes, q=q)


@colecoes_bp.route("/nova", methods=["GET", "POST"])
def nova():
    usuarios = Usuario.query.filter_by(ativo=True).order_by(Usuario.nome_completo).all()
    materiais = MaterialDidatico.query.filter_by(ativo=True).order_by(MaterialDidatico.titulo).all()
    if request.method == "POST":
        colecao = Colecao(
            nome=request.form["nome"],
            descricao=request.form.get("descricao") or None,
            visibilidade=request.form.get("visibilidade", "publica"),
            id_usuario_criador=int(request.form["id_usuario_criador"]),
        )
        db.session.add(colecao)
        db.session.flush()

        ids_materiais = request.form.getlist("materiais")
        for id_mat in ids_materiais:
            db.session.execute(
                material_colecao.insert().values(id_colecao=colecao.id_colecao, id_material=int(id_mat))
            )

        db.session.commit()
        flash(f"Coleção '{colecao.nome}' criada com sucesso!", "success")
        return redirect(url_for("colecoes.listar"))
    return render_template("colecoes/form.html", colecao=None, usuarios=usuarios, materiais=materiais, materiais_colecao=[])


@colecoes_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    colecao = Colecao.query.get_or_404(id)
    usuarios = Usuario.query.filter_by(ativo=True).order_by(Usuario.nome_completo).all()
    materiais = MaterialDidatico.query.filter_by(ativo=True).order_by(MaterialDidatico.titulo).all()

    if request.method == "POST":
        colecao.nome = request.form["nome"]
        colecao.descricao = request.form.get("descricao") or None
        colecao.visibilidade = request.form.get("visibilidade", "publica")
        colecao.id_usuario_criador = int(request.form["id_usuario_criador"])

        db.session.execute(
            material_colecao.delete().where(material_colecao.c.id_colecao == colecao.id_colecao)
        )
        ids_materiais = request.form.getlist("materiais")
        for id_mat in ids_materiais:
            db.session.execute(
                material_colecao.insert().values(id_colecao=colecao.id_colecao, id_material=int(id_mat))
            )

        db.session.commit()
        flash(f"Coleção '{colecao.nome}' atualizada!", "success")
        return redirect(url_for("colecoes.listar"))

    ids_na_colecao = [
        row.id_material
        for row in db.session.execute(
            material_colecao.select().where(material_colecao.c.id_colecao == colecao.id_colecao)
        )
    ]
    return render_template("colecoes/form.html", colecao=colecao, usuarios=usuarios, materiais=materiais, materiais_colecao=ids_na_colecao)


@colecoes_bp.route("/excluir/<int:id>", methods=["POST"])
def excluir(id):
    colecao = Colecao.query.get_or_404(id)
    colecao.ativa = False
    db.session.commit()
    flash("Coleção removida.", "success")
    return redirect(url_for("colecoes.listar"))
