from flask import Blueprint, render_template, request, redirect, url_for, flash
from database import db
from models import Usuario, Instituicao

usuarios_bp = Blueprint("usuarios", __name__)


@usuarios_bp.route("/")
def listar():
    q = request.args.get("q", "")
    tipo = request.args.get("tipo", "")
    ativo = request.args.get("ativo", "")

    query = Usuario.query

    if q:
        query = query.filter(Usuario.nome_completo.ilike(f"%{q}%") | Usuario.email.ilike(f"%{q}%"))
    if tipo:
        query = query.filter(Usuario.tipo == tipo)
    if ativo != "":
        query = query.filter(Usuario.ativo == (ativo == "true"))

    usuarios = query.order_by(Usuario.nome_completo).all()
    return render_template("usuarios/listar.html", usuarios=usuarios, q=q, tipo=tipo, ativo=ativo)


@usuarios_bp.route("/novo", methods=["GET", "POST"])
def novo():
    instituicoes = Instituicao.query.filter_by(ativa=True).all()
    if request.method == "POST":
        usuario = Usuario(
            nome_completo=request.form["nome_completo"],
            email=request.form["email"],
            senha=request.form["senha"],
            tipo=request.form["tipo"],
            id_instituicao=request.form.get("id_instituicao") or None,
            logradouro=request.form.get("logradouro"),
            numero=request.form.get("numero"),
            complemento=request.form.get("complemento"),
            bairro=request.form.get("bairro"),
            cidade_usuario=request.form.get("cidade_usuario"),
            estado_usuario=request.form.get("estado_usuario"),
            cep=request.form.get("cep"),
        )
        db.session.add(usuario)
        db.session.commit()
        flash("Usuário cadastrado com sucesso!", "success")
        return redirect(url_for("usuarios.listar"))
    return render_template("usuarios/form.html", usuario=None, instituicoes=instituicoes)


@usuarios_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    usuario = Usuario.query.get_or_404(id)
    instituicoes = Instituicao.query.filter_by(ativa=True).all()
    if request.method == "POST":
        usuario.nome_completo = request.form["nome_completo"]
        usuario.email = request.form["email"]
        usuario.tipo = request.form["tipo"]
        usuario.id_instituicao = request.form.get("id_instituicao") or None
        usuario.logradouro = request.form.get("logradouro")
        usuario.numero = request.form.get("numero")
        usuario.complemento = request.form.get("complemento")
        usuario.bairro = request.form.get("bairro")
        usuario.cidade_usuario = request.form.get("cidade_usuario")
        usuario.estado_usuario = request.form.get("estado_usuario")
        usuario.cep = request.form.get("cep")
        db.session.commit()
        flash("Usuário atualizado!", "success")
        return redirect(url_for("usuarios.listar"))
    return render_template("usuarios/form.html", usuario=usuario, instituicoes=instituicoes)


@usuarios_bp.route("/desativar/<int:id>", methods=["POST"])
def desativar(id):
    usuario = Usuario.query.get_or_404(id)
    usuario.ativo = not usuario.ativo
    db.session.commit()
    status = "reativado" if usuario.ativo else "desativado"
    flash(f"Usuário {status} com sucesso!", "success")
    return redirect(url_for("usuarios.listar"))
