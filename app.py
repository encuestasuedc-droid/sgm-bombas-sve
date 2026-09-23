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


@app.route("/dashboard")
def dashboard():

    total = Mantenimiento.query.count()

    costo_total = db.session.query(
        db.func.sum(Mantenimiento.costo)
    ).scalar()

    if costo_total is None:
        costo_total = 0

    return render_template(
        "dashboard.html",
        total=total,
        costo_total=costo_total
    )


if __name__ == "__main__":
    app.run()
