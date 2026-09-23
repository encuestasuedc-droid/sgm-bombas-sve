from flask import Flask, request
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

@app.route("/")
def inicio():

    return """
    <h1>SGM Bombas SVE v1.0</h1>

    <p><auevo🛠 Registrar mantenimiento</a></p>

    <p><a href="/hister historial</a></p>
    """

@app.route("/nuevo", methods=["GET","POST"])
def nuevo():

    if request.method == "POST":

        registro = Mantenimiento(
            fecha=request.form["fecha"],
            bomba=request.form["bomba"],
            componente=request.form["componente"],
            responsable=request.form["responsable"],
            costo=float(request.form["costo"]),
            observacion=request.form["observacion"]
        )

        db.session.add(registro)
        db.session.commit()

        return """
        <h2>✅ Registro guardado</h2>

        /Volver</a>
        """

    opciones = ""

    for i in range(1,24):
        opciones += f"<option>C{i}</option>"

    return f"""
    <h1>Nuevo mantenimiento</h1>

    <form method="post">

        Fecha<br>
        <input type="date" name="fecha"><br><br>

        Bomba<br>
        <select name="bomba">
        {opciones}
        </select><br><br>

        Componente<br>
        <select name="componente">

            <option>Comando eléctrico</option>
            <option>Cable y enchufe</option>
            <option>Motor</option>
            <option>Turbina</option>
            <option>Cabezal</option>
            <option>Rulemán</option>
            <option>Estopada</option>
            <option>Pintado</option>
            <option>Ruedas</option>

        </select><br><br>

        Responsable<br>
        <input type="text" name="responsable"><br><br>

        Costo<br>
        <input type="number" name="costo"><br><br>

        Observación<br>
        <textarea name="observacion"></textarea><br><br>

        <button type="submit">
            Guardar
        </button>

    </form>
    """

@app.route("/historial")
def historial():

    registros = Mantenimiento.query.all()

    html = """
    <h1>Historial</h1>

    
