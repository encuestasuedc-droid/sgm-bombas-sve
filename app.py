import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Obtiene la base PostgreSQL de Supabase desde Render.
# Si DATABASE_URL no existe, usa SQLite solamente como respaldo local.
database_url = os.environ.get("DATABASE_URL", "sqlite:///bombas.db")

# Compatibilidad con proveedores que entregan postgres://
if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_pre_ping": True,
    "pool_recycle": 280
}

db = SQLAlchemy(app)

class Mantenimiento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.String(20), nullable=False)
    bomba = db.Column(db.String(20), nullable=False)
    componente = db.Column(db.String(100), nullable=False)
    responsable = db.Column(db.String(100), nullable=False)
    costo = db.Column(db.Float, nullable=False, default=0.0)
    observacion = db.Column(db.String(500))

# Crea las tablas si no existen al iniciar la app
with app.app_context():
    db.create_all()

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/nuevo", methods=["GET", "POST"])
def nuevo():
    if request.method == "POST":
        costo_texto = request.form.get("costo", "0").strip()
        try:
            costo = float(costo_texto) if costo_texto else 0.0
        except ValueError:
            costo = 0.0

        nuevo_registro = Mantenimiento(
            fecha=request.form.get("fecha", "").strip(),
            bomba=request.form.get("bomba", "").strip(),
            componente=request.form.get("componente", "").strip(),
            responsable=request.form.get("responsable", "").strip(),
            costo=costo,
            observacion=request.form.get("observacion", "").strip()
        )
        
        try:
            db.session.add(nuevo_registro)
            db.session.commit()
            return redirect("/historial")
        except Exception as e:
            db.session.rollback()
            # Aquí podrías retornar un mensaje de error a la plantilla si la base de datos falla
            return f"Error al guardar en la base de datos: {e}", 500

    return render_template("registro.html")

@app.route("/historial")
def historial():
    bomba = request.args.get("bomba", "").strip()
    consulta = Mantenimiento.query
    
    if bomba:
        consulta = consulta.filter_by(bomba=bomba)
        
    registros = consulta.order_by(Mantenimiento.id.desc()).all()
    return render_template("historial.html", registros=registros)

@app.route("/dashboard")
def dashboard():
    total = Mantenimiento.query.count()
    costo_total = db.session.query(db.func.sum(Mantenimiento.costo)).scalar()
    
    if costo_total is None:
        costo_total = 0.0
        
    return render_template("dashboard.html", total=total, costo_total=costo_total)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0", 
        port=int(os.environ.get("PORT", 5000))
    )
