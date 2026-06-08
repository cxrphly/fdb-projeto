from flask import Blueprint, render_template, jsonify, request
from database import db
from sqlalchemy import func, case
from models import VotacaoUtilidade, MaterialDidatico, AvaliacaoMaterial, Disciplina, AcessoMaterial
from datetime import datetime, timedelta

graficos_bp = Blueprint("graficos", __name__)


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

