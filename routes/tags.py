from flask import Blueprint, render_template, request, redirect, url_for, flash
from database import db
from models import Tag, material_tag
from sqlalchemy import text

tags_bp = Blueprint("tags", __name__)


@tags_bp.route("/")
def listar():
    q = request.args.get("q", "")
    
    query = Tag.query
    if q:
        query = query.filter(Tag.nome_tag.ilike(f"%{q}%"))
    
    tags = query.order_by(Tag.nome_tag).all()
    return render_template("tags/listar.html", tags=tags, q=q)


@tags_bp.route("/nova", methods=["GET", "POST"])
def nova():
    if request.method == "POST":
        nome = request.form.get("nome_tag")
        
        existe = Tag.query.filter_by(nome_tag=nome).first()
        if existe:
            flash("Esta tag já está cadastrada!", "danger")
            return redirect(url_for("tags.nova"))
        
        tag = Tag(nome_tag=nome)
        db.session.add(tag)
        db.session.commit()
        flash("Tag cadastrada com sucesso!", "success")
        return redirect(url_for("tags.listar"))
    
    return render_template("tags/form.html", tag=None)


@tags_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    tag = Tag.query.get_or_404(id)
    
    if request.method == "POST":
        novo_nome = request.form.get("nome_tag")
        
        existe = Tag.query.filter(
            Tag.nome_tag == novo_nome,
            Tag.id_tag != id
        ).first()
        
        if existe:
            flash("Este nome de tag já está em uso!", "danger")
            return redirect(url_for("tags.editar", id=id))
        
        tag.nome_tag = novo_nome
        db.session.commit()
        flash("Tag atualizada com sucesso!", "success")
        return redirect(url_for("tags.listar"))
    
    return render_template("tags/form.html", tag=tag)


@tags_bp.route("/excluir/<int:id>", methods=["POST"])
def excluir(id):
    tag = Tag.query.get_or_404(id)
    
    # Verificar se a tag está sendo usada em algum material
    # Usando SQL direto para contar associações
    result = db.session.execute(
        text("SELECT COUNT(*) FROM material_tag WHERE id_tag = :tag_id"),
        {"tag_id": id}
    ).scalar()
    
    if result > 0:
        flash(f"Não é possível excluir esta tag pois ela está sendo usada em {result} materiais.", "danger")
        return redirect(url_for("tags.listar"))
    
    db.session.delete(tag)
    db.session.commit()
    flash("Tag excluída com sucesso!", "success")
    return redirect(url_for("tags.listar"))