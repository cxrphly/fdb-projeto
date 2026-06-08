# routes/menu.py
from flask import Blueprint, render_template
from database import db
from models import Usuario, MaterialDidatico, AvaliacaoMaterial, Denuncia

menu_bp = Blueprint("menu", __name__)

@menu_bp.route("/")
def index():
    try:
        stats = {
            'usuarios': Usuario.query.count(),
            'materiais': MaterialDidatico.query.count(),
            'avaliacoes': AvaliacaoMaterial.query.count(),
            'denuncias_pendentes': Denuncia.query.filter_by(status='pendente').count()
        }
        ultimos_usuarios = Usuario.query.order_by(Usuario.id_usuario.desc()).limit(5).all()
        
        ultimos_materiais = MaterialDidatico.query.filter_by(ativo=True).order_by(
            MaterialDidatico.id_material.desc()
        ).limit(5).all()
        
        print(f"DEBUG - Stats: {stats}")


        
        print(f"DEBUG - Usuários: {len(ultimos_usuarios)}")
        print(f"DEBUG - Materiais: {len(ultimos_materiais)}")
        
    except Exception as e:
        print(f"ERRO: {e}")
        stats = {'usuarios': 0, 'materiais': 0, 'avaliacoes': 0, 'denuncias_pendentes': 0}
        ultimos_usuarios = []
        ultimos_materiais = []
    
    return render_template(
        "menu.html",
        stats=stats,
        ultimos_usuarios=ultimos_usuarios,
        ultimos_materiais=ultimos_materiais
    )