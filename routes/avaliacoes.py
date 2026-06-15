from flask import Blueprint, render_template, request, redirect, url_for, flash
from database import db
from models import AvaliacaoMaterial, MaterialDidatico, Usuario

avaliacoes_bp = Blueprint("avaliacoes", __name__)


@avaliacoes_bp.route("/")
def listar():
    q = request.args.get("q", "")
    nota = request.args.get("nota", "")

    query = (
        db.session.query(AvaliacaoMaterial)
        .join(MaterialDidatico)
        .join(Usuario, AvaliacaoMaterial.id_usuario_avaliador == Usuario.id_usuario)
    )

    if q:
        query = query.filter(
            MaterialDidatico.titulo.ilike(f"%{q}%") | Usuario.nome_completo.ilike(f"%{q}%")
        )
    if nota:
        query = query.filter(AvaliacaoMaterial.nota == int(nota))

    avaliacoes = query.order_by(AvaliacaoMaterial.data_hora.desc()).all()
    return render_template("avaliacoes/listar.html", avaliacoes=avaliacoes, q=q, nota=nota)


@avaliacoes_bp.route("/nova", methods=["GET", "POST"])
def nova():
    materiais = MaterialDidatico.query.filter_by(ativo=True).order_by(MaterialDidatico.titulo).all()
    usuarios = Usuario.query.filter_by(ativo=True).order_by(Usuario.nome_completo).all()
    if request.method == "POST":
        id_material = int(request.form["id_material"])
        id_usuario = int(request.form["id_usuario_avaliador"])
        existente = AvaliacaoMaterial.query.filter_by(
            id_material=id_material, id_usuario_avaliador=id_usuario
        ).first()
        if existente:
            flash("Este usuário já avaliou este material.", "warning")
            return render_template("avaliacoes/form.html", avaliacao=None, materiais=materiais, usuarios=usuarios)
        avaliacao = AvaliacaoMaterial(
            nota=int(request.form["nota"]),
            comentario=request.form.get("comentario") or None,
            id_material=id_material,
            id_usuario_avaliador=id_usuario,
        )
        db.session.add(avaliacao)
        db.session.commit()
        flash(f"Avaliação de '{avaliacao.material.titulo}' registrada com sucesso!", "success")
        return redirect(url_for("avaliacoes.listar"))
    return render_template("avaliacoes/form.html", avaliacao=None, materiais=materiais, usuarios=usuarios)


@avaliacoes_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    avaliacao = AvaliacaoMaterial.query.get_or_404(id)
    materiais = MaterialDidatico.query.filter_by(ativo=True).order_by(MaterialDidatico.titulo).all()
    usuarios = Usuario.query.filter_by(ativo=True).order_by(Usuario.nome_completo).all()
    if request.method == "POST":
        avaliacao.nota = int(request.form["nota"])
        avaliacao.comentario = request.form.get("comentario") or None
        db.session.commit()
        flash(f"Avaliação de '{avaliacao.material.titulo}' atualizada!", "success")
        return redirect(url_for("avaliacoes.listar"))
    return render_template("avaliacoes/form.html", avaliacao=avaliacao, materiais=materiais, usuarios=usuarios)


@avaliacoes_bp.route("/excluir/<int:id>", methods=["POST"])
def excluir(id):
    avaliacao = AvaliacaoMaterial.query.get_or_404(id)
    db.session.delete(avaliacao)
    db.session.commit()
    flash("Avaliação removida.", "success")
    return redirect(url_for("avaliacoes.listar"))
