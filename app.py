from flask import Flask
from database import db
from routes.usuarios import usuarios_bp
from routes.materiais import materiais_bp
from routes.graficos import graficos_bp
from routes.menu import menu_bp
from routes.avaliacoes import avaliacoes_bp
from routes.favoritos import favoritos_bp
from routes.historico import historico_bp
from routes.colecoes import colecoes_bp


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql+psycopg2://postgres:1234@localhost:5432/postgres?options=-c%20search_path=fdb"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "projeto-fdb"

db.init_app(app)

app.register_blueprint(menu_bp)
app.register_blueprint(usuarios_bp, url_prefix="/usuarios")
app.register_blueprint(materiais_bp, url_prefix="/materiais")
app.register_blueprint(graficos_bp, url_prefix="/graficos")
app.register_blueprint(avaliacoes_bp, url_prefix="/avaliacoes")
app.register_blueprint(favoritos_bp, url_prefix="/favoritos")
app.register_blueprint(historico_bp, url_prefix="/historico")
app.register_blueprint(colecoes_bp, url_prefix="/colecoes")

if __name__ == "__main__":
    app.run(debug=True)