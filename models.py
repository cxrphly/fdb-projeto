from database import db
from datetime import datetime
class Instituicao(db.Model):
    __tablename__ = "instituicao"
    id_instituicao = db.Column(db.Integer, primary_key=True)
    nome_instituicao = db.Column(db.String(150), nullable=False, unique=True)
    sigla = db.Column(db.String(20))
    tipo = db.Column(db.String(20))
    pais = db.Column(db.String(50), default="brasil")
    estado = db.Column(db.String(50))
    cidade = db.Column(db.String(50))
    site = db.Column(db.String(200))
    ativa = db.Column(db.Boolean, default=True)
class Usuario(db.Model):
    __tablename__ = "usuario"
    id_usuario = db.Column(db.Integer, primary_key=True)
    nome_completo = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    senha = db.Column(db.String(255), nullable=False)
    tipo = db.Column(db.String(15))
    data_cadastro = db.Column(db.Date, default=datetime.utcnow)
    ativo = db.Column(db.Boolean, default=True)
    id_instituicao = db.Column(db.Integer, db.ForeignKey("fdb.instituicao.id_instituicao"))  # Adicionar fdb.
    logradouro = db.Column(db.String(150))
    numero = db.Column(db.String(10))
    complemento = db.Column(db.String(100))
    bairro = db.Column(db.String(100))
    cidade_usuario = db.Column(db.String(100))
    estado_usuario = db.Column(db.String(50))
    cep = db.Column(db.String(9))

    instituicao = db.relationship("Instituicao", backref="usuarios")


class Aluno(db.Model):
    __tablename__ = "aluno"
    id_usuario = db.Column(db.Integer, db.ForeignKey("fdb.usuario.id_usuario"), primary_key=True)  # Adicionar fdb.
    matricula_aluno = db.Column(db.String(20), nullable=False, unique=True)
    curso = db.Column(db.String(100))

    usuario = db.relationship("Usuario", backref=db.backref("aluno", uselist=False))





class Professor(db.Model):
    __tablename__ = "professor"
    id_usuario = db.Column(db.Integer, db.ForeignKey("fdb.usuario.id_usuario"), primary_key=True)  # Adicionar fdb.
    matricula_professor = db.Column(db.String(20), nullable=False, unique=True)

    usuario = db.relationship("Usuario", backref=db.backref("professor", uselist=False))



class Administrador(db.Model):
    __tablename__ = "administrador"
    id_usuario = db.Column(db.Integer, db.ForeignKey("fdb.usuario.id_usuario"), primary_key=True)  # Adicionar fdb.
    nivel_permissao = db.Column(db.Integer, nullable=False, default=1)

    usuario = db.relationship("Usuario", backref=db.backref("administrador", uselist=False))






class Disciplina(db.Model):
    __tablename__ = "disciplina"
    id_disciplina = db.Column(db.Integer, primary_key=True)
    nome_disciplina = db.Column(db.String(100), nullable=False, unique=True)


class Tag(db.Model):
    __tablename__ = "tag"
    id_tag = db.Column(db.Integer, primary_key=True)
    nome_tag = db.Column(db.String(50), nullable=False, unique=True)


material_tag = db.Table(
    "material_tag",
    db.Column("id_material", db.Integer, db.ForeignKey("fdb.materialdidatico.id_material"), primary_key=True),  # Adicionar fdb.
    db.Column("id_tag", db.Integer, db.ForeignKey("fdb.tag.id_tag"), primary_key=True),  # Adicionar fdb.
)
class MaterialDidatico(db.Model):
    __tablename__ = "materialdidatico"
    id_material = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    descricao = db.Column(db.Text)
    tipo_material = db.Column(db.String(15))
    arquivo_ou_link = db.Column(db.String(500), nullable=False)
    data_publicacao = db.Column(db.DateTime, default=datetime.utcnow)
    visibilidade = db.Column(db.String(10), default="publico")
    ativo = db.Column(db.Boolean, default=True)
    id_disciplina = db.Column(db.Integer, db.ForeignKey("fdb.disciplina.id_disciplina"), nullable=False)  # Adicionar fdb.
    id_autor = db.Column(db.Integer, db.ForeignKey("fdb.usuario.id_usuario"), nullable=False)  # Adicionar fdb.

    disciplina = db.relationship("Disciplina", backref="materiais")
    autor = db.relationship("Usuario", backref="materiais")
    tags = db.relationship("Tag", secondary=material_tag, backref="materiais")




class AvaliacaoMaterial(db.Model):
    __tablename__ = "avaliacaomaterial"
    id_avaliacao = db.Column(db.Integer, primary_key=True)
    nota = db.Column(db.Integer, nullable=False)
    comentario = db.Column(db.Text)
    data_hora = db.Column(db.DateTime, default=datetime.utcnow)
    id_material = db.Column(db.Integer, db.ForeignKey("fdb.materialdidatico.id_material"), nullable=False)  # Adicionar fdb.
    id_usuario_avaliador = db.Column(db.Integer, db.ForeignKey("fdb.usuario.id_usuario"), nullable=False)  # Adicionar fdb.

    __table_args__ = (db.UniqueConstraint("id_material", "id_usuario_avaliador"),)
    material = db.relationship("MaterialDidatico", backref="avaliacoes")
    avaliador = db.relationship("Usuario", backref="avaliacoes")


class Favorito(db.Model):
    __tablename__ = "favorito"
    id_favorito = db.Column(db.Integer, primary_key=True)
    data_adicao = db.Column(db.DateTime, default=datetime.utcnow)
    id_usuario = db.Column(db.Integer, db.ForeignKey("fdb.usuario.id_usuario"), nullable=False)  # Adicionar fdb.
    id_material = db.Column(db.Integer, db.ForeignKey("fdb.materialdidatico.id_material"), nullable=False)  # Adicionar fdb.

    __table_args__ = (db.UniqueConstraint("id_usuario", "id_material"),)
    usuario = db.relationship("Usuario", backref="favoritos")
    material = db.relationship("MaterialDidatico", backref="favoritado_por")


class Comentario(db.Model):
    __tablename__ = "comentario"
    id_comentario = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.Text, nullable=False)
    data_hora = db.Column(db.DateTime, default=datetime.utcnow)
    id_material = db.Column(db.Integer, db.ForeignKey("fdb.materialdidatico.id_material"), nullable=False)  # Adicionar fdb.
    id_usuario_autor = db.Column(db.Integer, db.ForeignKey("fdb.usuario.id_usuario"), nullable=False)  # Adicionar fdb.
    id_comentario_pai = db.Column(db.Integer, db.ForeignKey("fdb.comentario.id_comentario"))  # Adicionar fdb.

    material = db.relationship("MaterialDidatico", backref="comentarios")
    autor = db.relationship("Usuario", backref="comentarios")


class Denuncia(db.Model):
    __tablename__ = "denuncia"
    id_denuncia = db.Column(db.Integer, primary_key=True)
    motivo = db.Column(db.String(20))
    descricao_detalhada = db.Column(db.Text)
    data_hora = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(10), default="pendente")
    id_material = db.Column(db.Integer, db.ForeignKey("fdb.materialdidatico.id_material"), nullable=False)  # Adicionar fdb.
    id_usuario_denunciante = db.Column(db.Integer, db.ForeignKey("fdb.usuario.id_usuario"), nullable=False)  # Adicionar fdb.

    __table_args__ = (db.UniqueConstraint("id_material", "id_usuario_denunciante"),)
    material = db.relationship("MaterialDidatico", backref="denuncias")
    denunciante = db.relationship("Usuario", backref="denuncias")


class AcessoMaterial(db.Model):
    __tablename__ = "acessomaterial"
    id_acesso = db.Column(db.Integer, primary_key=True)
    data_hora_acesso = db.Column(db.DateTime, default=datetime.utcnow)
    oculto_no_historico = db.Column(db.Boolean, default=False)
    id_material = db.Column(db.Integer, db.ForeignKey("fdb.materialdidatico.id_material"), nullable=False)  # Adicionar fdb.
    id_usuario = db.Column(db.Integer, db.ForeignKey("fdb.usuario.id_usuario"), nullable=True)  # Adicionar fdb.

    material = db.relationship("MaterialDidatico", backref="acessos")
    usuario = db.relationship("Usuario", backref="acessos")

class VotacaoUtilidade(db.Model):
    __tablename__ = "votacaoutilidade"
    id_votacao = db.Column(db.Integer, primary_key=True)
    tipo_voto = db.Column(db.String(10))
    data_hora = db.Column(db.DateTime, default=datetime.utcnow)
    id_material = db.Column(db.Integer, db.ForeignKey("fdb.materialdidatico.id_material"), nullable=False)  # Adicionar fdb.
    id_usuario_votante = db.Column(db.Integer, db.ForeignKey("fdb.usuario.id_usuario"), nullable=False)  # Adicionar fdb.

    __table_args__ = (db.UniqueConstraint("id_material", "id_usuario_votante"),)
    material = db.relationship("MaterialDidatico", backref="votos")
    votante = db.relationship("Usuario", backref="votos")





class Colecao(db.Model):
    __tablename__ = "colecao"
    id_colecao = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    visibilidade = db.Column(db.String(10), default="publica")
    ativa = db.Column(db.Boolean, default=True)
    id_usuario_criador = db.Column(db.Integer, db.ForeignKey("fdb.usuario.id_usuario"), nullable=False)  # Adicionar fdb.

    criador = db.relationship("Usuario", backref="colecoes")



material_colecao = db.Table(
    "material_na_colecao",
    db.Column("id_colecao", db.Integer, db.ForeignKey("fdb.colecao.id_colecao"), primary_key=True),  # Adicionar fdb.
    db.Column("id_material", db.Integer, db.ForeignKey("fdb.materialdidatico.id_material"), primary_key=True),  # Adicionar fdb.
    db.Column("data_adicao", db.DateTime, default=datetime.utcnow),
)


class ProfessorDisciplina(db.Model):
    __tablename__ = "professor_disciplina"
    id_usuario = db.Column(db.Integer, db.ForeignKey("fdb.professor.id_usuario"), primary_key=True)  # Adicionar fdb.
    id_disciplina = db.Column(db.Integer, db.ForeignKey("fdb.disciplina.id_disciplina"), primary_key=True)  # Adicionar fdb.





class LinkCompartilhamento(db.Model):
    __tablename__ = "linkcompartilhamento"
    id_link_compartilhamento = db.Column(db.Integer, primary_key=True)
    token_unico = db.Column(db.String(64), nullable=False, unique=True)
    data_geracao = db.Column(db.DateTime, default=datetime.utcnow)
    data_expiracao = db.Column(db.DateTime)
    ativo = db.Column(db.Boolean, default=True)
    id_material = db.Column(db.Integer, db.ForeignKey("fdb.materialdidatico.id_material"), nullable=False)  # Adicionar fdb.

    material = db.relationship("MaterialDidatico", backref="links")