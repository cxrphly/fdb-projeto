from flask import Blueprint, render_template, request, redirect, url_for, flash
from database import db
from models import Disciplina, MaterialDidatico

disciplinas_bp = Blueprint("disciplinas", __name__)


@disciplinas_bp.route("/")
def listar():
    q = request.args.get("q", "")
    
    query = Disciplina.query
    if q:
        query = query.filter(Disciplina.nome_disciplina.ilike(f"%{q}%"))
    
    disciplinas = query.order_by(Disciplina.nome_disciplina).all()
    return render_template("disciplinas/listar.html", disciplinas=disciplinas, q=q)


@disciplinas_bp.route("/nova", methods=["GET", "POST"])
def nova():
    if request.method == "POST":
        nome = request.form.get("nome_disciplina")
        
        existe = Disciplina.query.filter_by(nome_disciplina=nome).first()
        if existe:
            flash("Esta disciplina já está cadastrada!", "danger")
            return redirect(url_for("disciplinas.nova"))
        
        disciplina = Disciplina(nome_disciplina=nome)
        db.session.add(disciplina)
        db.session.commit()
        flash("Disciplina cadastrada com sucesso!", "success")
        return redirect(url_for("disciplinas.listar"))
    
    return render_template("disciplinas/form.html", disciplina=None)


@disciplinas_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    disciplina = Disciplina.query.get_or_404(id)
    
    if request.method == "POST":
        novo_nome = request.form.get("nome_disciplina")
        
        existe = Disciplina.query.filter(
            Disciplina.nome_disciplina == novo_nome,
            Disciplina.id_disciplina != id
        ).first()
        
        if existe:
            flash("Este nome de disciplina já está em uso!", "danger")
            return redirect(url_for("disciplinas.editar", id=id))
        
        disciplina.nome_disciplina = novo_nome
        db.session.commit()
        flash("Disciplina atualizada com sucesso!", "success")
        return redirect(url_for("disciplinas.listar"))
    
    return render_template("disciplinas/form.html", disciplina=disciplina)


@disciplinas_bp.route("/excluir/<int:id>", methods=["POST"])
def excluir(id):
    disciplina = Disciplina.query.get_or_404(id)
    
    materiais_associados = MaterialDidatico.query.filter_by(id_disciplina=id).count()
    if materiais_associados > 0:
        flash(f"Não é possível excluir esta disciplina pois existem {materiais_associados} materiais vinculados a ela.", "danger")
        return redirect(url_for("disciplinas.listar"))
    
    db.session.delete(disciplina)
    db.session.commit()
    flash("Disciplina excluída com sucesso!", "success")
    return redirect(url_for("disciplinas.listar"))