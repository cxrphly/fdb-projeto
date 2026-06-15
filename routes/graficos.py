from flask import Blueprint, render_template, jsonify, request
from database import db
from sqlalchemy import func, case
from models import VotacaoUtilidade, MaterialDidatico, AvaliacaoMaterial, AcessoMaterial
from datetime import datetime, timedelta

graficos_bp = Blueprint("graficos", __name__)


def _get_periodo_filter(model_col):
    periodo = request.args.get("periodo", "all")
    if periodo == "7":
        return model_col >= datetime.utcnow() - timedelta(days=7)
    if periodo == "30":
        return model_col >= datetime.utcnow() - timedelta(days=30)
    if periodo == "90":
        return model_col >= datetime.utcnow() - timedelta(days=90)
    return None


@graficos_bp.route("/votos")
def votos():
    return render_template("graficos/votos.html")


@graficos_bp.route("/votos/dados")
def votos_dados():
    resultados = (
        db.session.query(
            MaterialDidatico.titulo,
            func.coalesce(func.sum(case((VotacaoUtilidade.tipo_voto == "util", 1), else_=0)), 0).label("uteis"),
            func.coalesce(func.sum(case((VotacaoUtilidade.tipo_voto == "nao_util", 1), else_=0)), 0).label("nao_uteis"),
        )
        .outerjoin(VotacaoUtilidade, MaterialDidatico.id_material == VotacaoUtilidade.id_material)
        .filter(MaterialDidatico.ativo == True)
        .group_by(MaterialDidatico.id_material, MaterialDidatico.titulo)
        .order_by(func.coalesce(func.sum(case((VotacaoUtilidade.tipo_voto == "util", 1), else_=0)), 0).desc())
        .limit(10)
        .all()
    )
    
    for r in resultados:
        print(f"  - {r.titulo}: úteis={r.uteis}, não úteis={r.nao_uteis}")
    
    return jsonify({
        "labels": [r.titulo[:30] for r in resultados if r.uteis > 0 or r.nao_uteis > 0],
        "uteis": [r.uteis for r in resultados if r.uteis > 0 or r.nao_uteis > 0],
        "nao_uteis": [r.nao_uteis for r in resultados if r.uteis > 0 or r.nao_uteis > 0],
    })


@graficos_bp.route("/notas")
def notas():
    return render_template("graficos/notas.html")


@graficos_bp.route("/notas/dados")
def notas_dados():
    periodo = request.args.get("periodo", "all")
    q = db.session.query(
        MaterialDidatico.titulo,
        func.round(func.avg(AvaliacaoMaterial.nota), 2).label("media"),
        func.count(AvaliacaoMaterial.id_avaliacao).label("contagem"),
    ).join(AvaliacaoMaterial, MaterialDidatico.id_material == AvaliacaoMaterial.id_material).filter(MaterialDidatico.ativo == True)

    filtro = _get_periodo_filter(AvaliacaoMaterial.data_hora)
    if filtro is not None:
        q = q.filter(filtro)

    resultados = q.group_by(MaterialDidatico.id_material, MaterialDidatico.titulo).order_by(func.count(AvaliacaoMaterial.id_avaliacao).desc()).limit(10).all()

    total_q = db.session.query(func.count(AvaliacaoMaterial.id_avaliacao))
    if filtro is not None:
        total_q = total_q.filter(filtro)
    total = total_q.scalar() or 0

    return jsonify({
        "labels": [r.titulo[:30] for r in resultados],
        "medias": [float(r.media) for r in resultados],
        "contagens": [r.contagem for r in resultados],
        "total_avaliacoes": total,
        "periodo": periodo,
    })


@graficos_bp.route("/acessos")
def acessos():
    return render_template("graficos/acessos.html")


@graficos_bp.route("/acessos/dados")
def acessos_dados():
    periodo = request.args.get("periodo", "all")
    filtro = _get_periodo_filter(AcessoMaterial.data_hora_acesso)

    q = db.session.query(
        MaterialDidatico.titulo,
        func.count(AcessoMaterial.id_acesso).label("total"),
    ).join(AcessoMaterial, MaterialDidatico.id_material == AcessoMaterial.id_material).filter(MaterialDidatico.ativo == True)
    if filtro is not None:
        q = q.filter(filtro)
    resultados = q.group_by(MaterialDidatico.id_material, MaterialDidatico.titulo).order_by(func.count(AcessoMaterial.id_acesso).desc()).limit(10).all()

    total_q = db.session.query(func.count(AcessoMaterial.id_acesso))
    id_q = db.session.query(func.count(AcessoMaterial.id_acesso)).filter(AcessoMaterial.id_usuario != None)
    if filtro is not None:
        total_q = total_q.filter(filtro)
        id_q = id_q.filter(filtro)
    total_acessos = total_q.scalar() or 0
    identificados = id_q.scalar() or 0

    return jsonify({
        "labels": [r.titulo[:30] for r in resultados],
        "acessos": [r.total for r in resultados],
        "total_acessos": total_acessos,
        "identificados": identificados,
        "anonimos": total_acessos - identificados,
        "periodo": periodo,
    })

