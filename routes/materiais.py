from flask import Blueprint, render_template, request, redirect, url_for, flash
from database import db
from models import MaterialDidatico, Usuario, Disciplina, Tag

materiais_bp = Blueprint("materiais", __name__)

PER_PAGE = 12

@materiais_bp.route("/")
def listar():
    q = request.args.get("q", "")
    tipo = request.args.get("tipo", "")
    id_disciplina = request.args.get("id_disciplina", "")
    page = request.args.get("page", 1, type=int)

    query = MaterialDidatico.query.filter_by(ativo=True)
    if q:
        query = query.filter(MaterialDidatico.titulo.ilike(f"%{q}%"))
    if tipo:
        query = query.filter(MaterialDidatico.tipo_material == tipo)
    if id_disciplina:
        query = query.filter(MaterialDidatico.id_disciplina == id_disciplina)

    paginacao = query.order_by(MaterialDidatico.data_publicacao.desc()).paginate(page=page, per_page=PER_PAGE, error_out=False)
    disciplinas = Disciplina.query.order_by(Disciplina.nome_disciplina).all()
    return render_template("materiais/listar.html", materiais=paginacao.items, paginacao=paginacao,
                           disciplinas=disciplinas, q=q, tipo=tipo, id_disciplina=id_disciplina)

@materiais_bp.route("/novo", methods=["GET", "POST"])
def novo():
    disciplinas = Disciplina.query.all()
    tags = Tag.query.all()
    autores = Usuario.query.filter_by(ativo=True).all()
    if request.method == "POST":
        material = MaterialDidatico(
            titulo=request.form["titulo"],
            descricao=request.form.get("descricao"),
            tipo_material=request.form["tipo_material"],
            arquivo_ou_link=request.form["arquivo_ou_link"],
            visibilidade=request.form.get("visibilidade", "publico"),
            id_disciplina=request.form["id_disciplina"],
            id_autor=request.form["id_autor"],
        )
        tag_ids = request.form.getlist("tags")
        for tid in tag_ids:
            tag = Tag.query.get(tid)
            if tag:
                material.tags.append(tag)
        db.session.add(material)
        db.session.commit()
        flash(f"Material '{material.titulo}' publicado com sucesso!", "success")
        return redirect(url_for("materiais.listar"))
    return render_template("materiais/form.html", material=None, disciplinas=disciplinas, tags=tags, autores=autores)


@materiais_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    material = MaterialDidatico.query.get_or_404(id)
    disciplinas = Disciplina.query.all()
    tags = Tag.query.all()
    autores = Usuario.query.filter_by(ativo=True).all()
    if request.method == "POST":
        material.titulo = request.form["titulo"]
        material.descricao = request.form.get("descricao")
        material.tipo_material = request.form["tipo_material"]
        material.arquivo_ou_link = request.form["arquivo_ou_link"]
        material.visibilidade = request.form.get("visibilidade", "publico")
        material.id_disciplina = request.form["id_disciplina"]
        material.tags = []
        for tid in request.form.getlist("tags"):
            tag = Tag.query.get(tid)
            if tag:
                material.tags.append(tag)
        db.session.commit()
        flash(f"Material '{material.titulo}' atualizado!", "success")
        return redirect(url_for("materiais.listar"))
    return render_template("materiais/form.html", material=material, disciplinas=disciplinas, tags=tags, autores=autores)






@materiais_bp.route("/excluidos")
def excluidos():
    materiais = MaterialDidatico.query.filter_by(ativo=False).order_by(MaterialDidatico.data_publicacao.desc()).all()
    return render_template("materiais/excluidos.html", materiais=materiais)


@materiais_bp.route("/restaurar/<int:id>", methods=["POST"])
def restaurar(id):
    material = MaterialDidatico.query.get_or_404(id)
    material.ativo = True
    db.session.commit()
    flash(f"Material '{material.titulo}' restaurado com sucesso!", "success")
    return redirect(url_for("materiais.excluidos"))


@materiais_bp.route("/excluir/<int:id>", methods=["POST"])
def excluir(id):
    material = MaterialDidatico.query.get_or_404(id)
    titulo = material.titulo
    material.ativo = False
    db.session.commit()
    flash(f"Material '{titulo}' removido. Você pode restaurá-lo em 'Ver Excluídos'.", "warning")
    return redirect(url_for("materiais.listar"))

@materiais_bp.route("/compartilhar/<int:id>", methods=["GET", "POST"])
def compartilhar(id):
    from models import LinkCompartilhamento
    import secrets
    from datetime import datetime, timedelta
    
    material = MaterialDidatico.query.get_or_404(id)
    
    if request.method == "POST":
        data_expiracao_str = request.form.get("data_expiracao")
        data_expiracao = None
        if data_expiracao_str:
            data_expiracao = datetime.strptime(data_expiracao_str, "%Y-%m-%d")
        
        token = secrets.token_urlsafe(32)
        
        link = LinkCompartilhamento(
            token_unico=token,
            data_expiracao=data_expiracao,
            ativo=True,
            id_material=material.id_material
        )
        db.session.add(link)
        db.session.commit()
        flash("Link de compartilhamento gerado com sucesso!", "success")
        return redirect(url_for("materiais.compartilhar", id=material.id_material))
    
    links_ativos = LinkCompartilhamento.query.filter_by(
        id_material=material.id_material,
        ativo=True
    ).all()
    
    return render_template("materiais/compartilhar.html", material=material, links_ativos=links_ativos)



@materiais_bp.route("/acessar_link/<token>")
def acessar_link(token):
    from models import LinkCompartilhamento, AcessoMaterial
    from datetime import datetime
    
    link = LinkCompartilhamento.query.filter_by(token_unico=token, ativo=True).first()
    
    if not link:
        flash("Link inválido ou desativado.", "danger")
        return redirect(url_for("materiais.listar"))
    
    if link.data_expiracao and link.data_expiracao < datetime.utcnow():
        flash("Este link expirou.", "danger")
        return redirect(url_for("materiais.listar"))
    
    material = link.material
    
    acesso = AcessoMaterial(
        id_material=material.id_material,
        id_usuario=None,  # Anônimo
        data_hora_acesso=datetime.utcnow(),
        oculto_no_historico=False
    )
    db.session.add(acesso)
    db.session.commit()
    
    return redirect(material.arquivo_ou_link)


@materiais_bp.route("/desativar_link/<int:id>", methods=["POST"])
def desativar_link(id):
    from models import LinkCompartilhamento
    
    link = LinkCompartilhamento.query.get_or_404(id)
    link.ativo = False
    db.session.commit()
    flash("Link desativado com sucesso!", "success")
    return redirect(url_for("materiais.compartilhar", id=link.id_material))


@materiais_bp.route("/visualizar/<int:id>")
def visualizar(id):
    from datetime import datetime
    
    material = MaterialDidatico.query.get_or_404(id)
    
    from models import AcessoMaterial
    acesso = AcessoMaterial(
        id_material=material.id_material,
        id_usuario=None,
        data_hora_acesso=datetime.utcnow(),
        oculto_no_historico=False
    )
    db.session.add(acesso)
    db.session.commit()
    
    return redirect(material.arquivo_ou_link)





@materiais_bp.route("/sugestoes")
def sugestoes():
    from models import AcessoMaterial, Disciplina
    from sqlalchemy import func
    
    sugestoes = db.session.query(
        MaterialDidatico,
        func.count(AcessoMaterial.id_acesso).label('total_acessos')
    ).outerjoin(
        AcessoMaterial, MaterialDidatico.id_material == AcessoMaterial.id_material
    ).filter(
        MaterialDidatico.ativo == True
    ).group_by(
        MaterialDidatico.id_material
    ).order_by(
        func.count(AcessoMaterial.id_acesso).desc()
    ).limit(9).all()
    
    disciplinas_com_materiais = db.session.query(
        Disciplina,
        func.count(MaterialDidatico.id_material).label('total')
    ).join(
        MaterialDidatico, Disciplina.id_disciplina == MaterialDidatico.id_disciplina
    ).filter(
        MaterialDidatico.ativo == True
    ).group_by(
        Disciplina.id_disciplina
    ).order_by(
        func.count(MaterialDidatico.id_material).desc()
    ).limit(6).all()
    
    disciplinas_materiais = []
    for d in disciplinas_com_materiais:
        disciplina_obj = d[0]
        materiais_disc = MaterialDidatico.query.filter_by(
            id_disciplina=disciplina_obj.id_disciplina,
            ativo=True
        ).limit(3).all()
        disciplinas_materiais.append({
            'disciplina': disciplina_obj.nome_disciplina,
            'materiais': materiais_disc
        })
    
    for s in sugestoes:
        if hasattr(s, 'total_acessos'):
            s[0].score = min(100, int(s[1] / 100) if s[1] else 50)
            s[0].acessos = s[1] or 0
        else:
            s[0].score = 85
            s[0].acessos = 0
    
    return render_template(
        "materiais/sugestoes.html",
        sugestoes=[s[0] for s in sugestoes if hasattr(s, '__getitem__')],
        por_disciplina=disciplinas_materiais
    )








@materiais_bp.route("/importar", methods=["GET", "POST"])
def importar():
    from models import Disciplina, Usuario
    import re
    from urllib.parse import urlparse
    
    disciplinas = Disciplina.query.order_by(Disciplina.nome_disciplina).all()
    autores = Usuario.query.filter_by(ativo=True).all()
    
    if request.method == "POST":
        url = request.form.get("url")
        titulo = request.form.get("titulo")
        id_disciplina = request.form.get("id_disciplina")
        id_autor = request.form.get("id_autor")
        visibilidade = request.form.get("visibilidade", "publico")
        tipo_material = "link_externo"
        if "youtube.com" in url or "youtu.be" in url:
            tipo_material = "video"
        elif "vimeo.com" in url:
            tipo_material = "video"
        elif url.endswith(".pdf"):
            tipo_material = "apostila"
        if not titulo:
            titulo = urlparse(url).path.split("/")[-1] or "Material Importado"
            titulo = titulo.replace("_", " ").replace("-", " ").title()
        
        material = MaterialDidatico(
            titulo=titulo,

            descricao=f"Material importado de: {url}",
            tipo_material=tipo_material,
            arquivo_ou_link=url,
            visibilidade=visibilidade,
            id_disciplina=id_disciplina,
            id_autor=id_autor,
            ativo=True
        )
    

        db.session.add(material)
        db.session.commit()
        flash(f"Material '{titulo}' importado com sucesso!", "success")
        return redirect(url_for("materiais.listar"))
    
    return render_template(
        "materiais/importar.html",
        disciplinas=disciplinas,
        autores=autores,
        importacoes_recentes=[]
    )





