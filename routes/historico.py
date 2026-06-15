from flask import Blueprint, render_template, request, redirect, url_for, flash
from database import db
from models import AcessoMaterial, MaterialDidatico, Usuario

historico_bp = Blueprint("historico", __name__)


@historico_bp.route("/")
def listar():
    q = request.args.get("q", "")
    id_usuario = request.args.get("id_usuario", "")

    query = (
        db.session.query(AcessoMaterial)
        .join(MaterialDidatico, AcessoMaterial.id_material == MaterialDidatico.id_material)
        .outerjoin(Usuario, AcessoMaterial.id_usuario == Usuario.id_usuario)
        .filter(AcessoMaterial.oculto_no_historico == False)
    )

    if q:
        query = query.filter(MaterialDidatico.titulo.ilike(f"%{q}%"))
    if id_usuario:
        query = query.filter(AcessoMaterial.id_usuario == int(id_usuario))

    acessos = query.order_by(AcessoMaterial.data_hora_acesso.desc()).limit(200).all()
    usuarios = Usuario.query.filter_by(ativo=True).order_by(Usuario.nome_completo).all()
    return render_template("historico/listar.html", acessos=acessos, q=q, id_usuario=id_usuario, usuarios=usuarios)


@historico_bp.route("/ocultar/<int:id>", methods=["POST"])
def ocultar(id):
    acesso = AcessoMaterial.query.get_or_404(id)
    acesso.oculto_no_historico = True
    db.session.commit()
    flash("Registro ocultado do histórico.", "success")
    return redirect(url_for("historico.listar"))
