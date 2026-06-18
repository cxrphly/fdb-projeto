from flask import Blueprint, render_template, request, redirect, url_for, flash
from database import db
from models import Comentario, MaterialDidatico, Usuario

comentarios_bp = Blueprint("comentarios", __name__)


@comentarios_bp.route("/")
def listar():
    id_material = request.args.get("id_material", "")

    query = Comentario.query
    if id_material:
        query = query.filter(Comentario.id_material == id_material)

    comentarios = query.order_by(Comentario.data_hora.asc()).all()
    materiais = MaterialDidatico.query.filter_by(ativo=True).all()
    return render_template("comentarios/listar.html", comentarios=comentarios, materiais=materiais, id_material=id_material)


@comentarios_bp.route("/novo", methods=["GET", "POST"])
def novo():
    materiais = MaterialDidatico.query.filter_by(ativo=True).all()
    usuarios = Usuario.query.filter_by(ativo=True).all()
    comentarios_pai = Comentario.query.all()
    if request.method == "POST":
        c = Comentario(
            texto=request.form["texto"],
            id_material=request.form["id_material"],
            id_usuario_autor=request.form["id_usuario_autor"],
            id_comentario_pai=request.form.get("id_comentario_pai") or None,
        )
        db.session.add(c)
        db.session.commit()
        flash("Comentário adicionado!", "success")
        return redirect(url_for("comentarios.listar"))
    return render_template("comentarios/form.html", comentario=None, materiais=materiais,
                           usuarios=usuarios, comentarios_pai=comentarios_pai)


@comentarios_bp.route("/excluir/<int:id>", methods=["POST"])
def excluir(id):
    c = Comentario.query.get_or_404(id)
    db.session.delete(c)
    db.session.commit()
    flash("Comentário removido.", "warning")
    return redirect(url_for("comentarios.listar"))
