import os

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


# Obtener la URL de Supabase desde Render.
# Si DATABASE_URL no existe, usar SQLite como respaldo local.
database_url = os.environ.get(
    "DATABASE_URL",
    "sqlite:///bombas.db"
)


# Configurar Psycopg 3 para PostgreSQL.
if database_url.startswith("postgres://"):
    database_url = database_url.replace(
        "postgres://",
        "postgresql+psycopg://",
        1
    )

elif database_url.startswith("postgresql://"):
    database_url = database_url.replace(
        "postgresql://",
        "postgresql+psycopg://",
        1
    )


app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_pre_ping": True,
    "pool_recycle": 280
}


db = SQLAlchemy(app)


# Modelo de mantenimientos
class Mantenimiento(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    fecha = db.Column(
        db.String(20),
        nullable=False
    )

    bomba = db.Column(
        db.String(20),
        nullable=False
    )

    componente = db.Column(
        db.String(100),
        nullable=False
    )

    responsable = db.Column(
        db.String(100),
        nullable=False
    )

    costo = db.Column(
        db.Float,
        nullable=False,
        default=0.0
    )

    observacion = db.Column(
        db.String(500)
    )


# Crear las tablas si todavía no existen
with app.app_context():
    db.create_all()


# Pantalla de inicio
@app.route("/")
def inicio():
    return render_template("inicio.html")


# Registrar mantenimiento
@app.route("/nuevo", methods=["GET", "POST"])
def nuevo():

    if request.method == "POST":

        costo_texto = request.form.get(
            "costo",
            "0"
        ).strip()

        try:
            costo = (
                float(costo_texto)
                if costo_texto
                else 0.0
            )
        except ValueError:
            costo = 0.0

        nuevo_registro = Mantenimiento(
            fecha=request.form.get(
                "fecha",
                ""
            ).strip(),
            bomba=request.form.get(
                "bomba",
                ""
            ).strip(),
            componente=request.form.get(
                "componente",
                ""
            ).strip(),
            responsable=request.form.get(
                "responsable",
                ""
            ).strip(),
            costo=costo,
            observacion=request.form.get(
                "observacion",
                ""
            ).strip()
        )

        try:
            db.session.add(nuevo_registro)
            db.session.commit()

            return redirect("/historial")

        except Exception:
            db.session.rollback()

            app.logger.exception(
                "Error al guardar el mantenimiento"
            )

            return (
                "No se pudo guardar el mantenimiento. "
                "Revisá la conexión con la base de datos.",
        
