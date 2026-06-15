from flask import Blueprint, render_template, request, redirect, url_for, flash
from database import db
from models import Favorito, MaterialDidatico, Usuario

favoritos_bp = Blueprint("favoritos", __name__)


@favoritos_bp.route("/")
def listar():
    q = request.args.get("q", "")

    query = (
        db.session.query(Favorito)
        .join(Usuario, Favorito.id_usuario == Usuario.id_usuario)
        .join(MaterialDidatico, Favorito.id_material == MaterialDidatico.id_material)
    )

    if q:
        query = query.filter(
            Usuario.nome_completo.ilike(f"%{q}%") | MaterialDidatico.titulo.ilike(f"%{q}%")
        )

    favoritos = query.order_by(Favorito.data_adicao.desc()).all()
    return render_template("favoritos/listar.html", favoritos=favoritos, q=q)


@favoritos_bp.route("/novo", methods=["GET", "POST"])
def novo():
    materiais = MaterialDidatico.query.filter_by(ativo=True).order_by(MaterialDidatico.titulo).all()
    usuarios = Usuario.query.filter_by(ativo=True).order_by(Usuario.nome_completo).all()
    if request.method == "POST":
        id_material = int(request.form["id_material"])
        id_usuario = int(request.form["id_usuario"])
        existente = Favorito.query.filter_by(id_usuario=id_usuario, id_material=id_material).first()
        if existente:
            flash("Este material já está nos favoritos do usuário.", "warning")
            return render_template("favoritos/form.html", materiais=materiais, usuarios=usuarios)
        favorito = Favorito(id_usuario=id_usuario, id_material=id_material)
        db.session.add(favorito)
        db.session.commit()
        flash("Favorito adicionado com sucesso!", "success")
        return redirect(url_for("favoritos.listar"))
    return render_template("favoritos/form.html", materiais=materiais, usuarios=usuarios)


@favoritos_bp.route("/excluir/<int:id>", methods=["POST"])
def excluir(id):
    favorito = Favorito.query.get_or_404(id)
    db.session.delete(favorito)
    db.session.commit()
    flash("Favorito removido.", "success")
    return redirect(url_for("favoritos.listar"))
