from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bombas.db"

db = SQLAlchemy(app)

class Mantenimiento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.String(20))
    bomba = db.Column(db.String(20))
    componente = db.Column(db.String(100))
    responsable = db.Column(db.String(100))
    costo = db.Column(db.Float)
    observacion = db.Column(db.String(500))

with app.app_context():
    db.create_all()

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/nuevo", methods=["GET", "POST"])
def nuevo():

    if request.method == "POST":

        nuevo_registro = Mantenimiento(
            fecha=request.form["fecha"],
            bomba=request.form["bomba"],
            componente=request.form["componente"],
            responsable=request.form["responsable"],
            costo=float(request.form["costo"]),
            observacion=request.form["observacion"]
        )

        db.session.add(nuevo_registro)
        db.session.commit()

        return redirect("/historial")

    return render_template("registro.html")

@app.route("/historial")
def historial():

    registros = Mantenimiento.query.order_by(
        Mantenimiento.id.desc()
    ).all()

    return render_template(
        "historial.html",
        registros=registros
    )

    for r in registros:

        html += f"""
        <p>
        <b>Fecha:</b> {r.fecha}<br>
        <b>Bomba:</b> {r.bomba}<br>
        <b>Componente:</b> {r.componente}<br>
        <b>Responsable:</b> {r.responsable}<br>
        <b>Costo:</b> ${r.costo}<br>
        <b>Observación:</b> {r.observacion}
        </p>
        <hr>
        """

    return html

if __name__ == "__main__":
    app.run()
