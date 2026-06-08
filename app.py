from flask import Flask
from database import db
from routes.usuarios import usuarios_bp
from routes.materiais import materiais_bp
from routes.graficos import graficos_bp
from routes.menu import menu_bp


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql+psycopg2://postgres@localhost:5432/postgres?options=-c%20search_path=fdb"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "projeto-fdb"

db.init_app(app)

app.register_blueprint(menu_bp)
app.register_blueprint(usuarios_bp, url_prefix="/usuarios")
app.register_blueprint(materiais_bp, url_prefix="/materiais")
app.register_blueprint(graficos_bp, url_prefix="/graficos")

if __name__ == "__main__":
    app.run(debug=True)