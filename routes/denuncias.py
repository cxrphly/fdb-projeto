from flask import Blueprint, render_template, request, redirect, url_for, flash
from database import db
from models import Denuncia, MaterialDidatico, Usuario

denuncias_bp = Blueprint("denuncias", __name__)


@denuncias_bp.route("/")
def listar():
    status = request.args.get("status", "")
    id_material = request.args.get("id_material", "")

    query = Denuncia.query
    if status:
        query = query.filter(Denuncia.status == status)
    if id_material:
        query = query.filter(Denuncia.id_material == id_material)

    denuncias = query.order_by(Denuncia.data_hora.desc()).all()
    materiais = MaterialDidatico.query.all()
    return render_template("denuncias/listar.html", denuncias=denuncias, materiais=materiais,
                           status=status, id_material=id_material)


@denuncias_bp.route("/nova", methods=["GET", "POST"])
def nova():
    materiais = MaterialDidatico.query.filter_by(ativo=True).all()
    usuarios = Usuario.query.filter_by(ativo=True).all()
    if request.method == "POST":
        existente = Denuncia.query.filter_by(
            id_material=request.form["id_material"],
            id_usuario_denunciante=request.form["id_usuario_denunciante"]
        ).first()
        if existente:
            flash("Este usuário já denunciou este material.", "danger")
            return redirect(url_for("denuncias.nova"))
        d = Denuncia(
            motivo=request.form["motivo"],
            descricao_detalhada=request.form.get("descricao_detalhada"),
            id_material=request.form["id_material"],
            id_usuario_denunciante=request.form["id_usuario_denunciante"],
        )
        db.session.add(d)
        db.session.commit()
        flash("Denúncia registrada!", "success")
        return redirect(url_for("denuncias.listar"))
    return render_template("denuncias/form.html", materiais=materiais, usuarios=usuarios)


@denuncias_bp.route("/moderar/<int:id>", methods=["POST"])
def moderar(id):
    d = Denuncia.query.get_or_404(id)
    novo_status = request.form["status"]
    d.status = novo_status
    db.session.commit()

    # Se aprovada, verifica se o material tem 3+ denúncias aprovadas
    if novo_status == "aprovada":
        aprovadas = Denuncia.query.filter_by(id_material=d.id_material, status="aprovada").count()
        if aprovadas >= 3:
            material = MaterialDidatico.query.get(d.id_material)
            if material:
                material.ativo = False
                db.session.commit()
                flash("Material desativado automaticamente (3 denúncias aprovadas).", "danger")

    flash(f"Denúncia marcada como '{novo_status}'.", "success")
    return redirect(url_for("denuncias.listar"))


@denuncias_bp.route("/excluir/<int:id>", methods=["POST"])
def excluir(id):
    d = Denuncia.query.get_or_404(id)
    db.session.delete(d)
    db.session.commit()
    flash("Denúncia removida.", "warning")
    return redirect(url_for("denuncias.listar"))
