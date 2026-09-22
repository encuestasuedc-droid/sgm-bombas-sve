from flask import Flask, request

app = Flask(__name__)

# Base simple en memoria (paso previo a SQLite)
registros = []

@app.route("/")
def inicio():
    return """
    <h1>SGM Bombas SVE v1.0</h1>

    <p>/nuevo🛠 Registrar mantenimiento</a></p>

    <p><historial📋 Ver historial</a></p>
    """


@app.route("/nuevo", methods=["GET", "POST"])
def nuevo():

    if request.method == "POST":

        registros.append(
            {
                "fecha": request.form["fecha"],
                "bomba": request.form["bomba"],
                "componente": request.form["componente"],
                "responsable": request.form["responsable"],
                "costo": request.form["costo"],
                "observacion": request.form["observacion"],
            }
        )

        return """
        <h2>✅ Registro guardado</h2>

        /
            Volver al inicio
        </a>
        """

    opciones = ""

    for i in range(1, 24):
        opciones += f"<option>C{i}</option>"

    return f"""
    <h1>Nuevo mantenimiento</h1>

    <form method='post'>

        <p>Fecha</p>
        <input type='date' name='fecha' required>

        <p>Bomba</p>
        <select name='bomba'>
            {opciones}
        </select>

        <p>Componente</p>
        <select name='componente'>
            <option>Comando eléctrico</option>
            <option>Cable y enchufe</option>
            <option>Motor</option>
            <option>Turbina</option>
            <option>Cabezal</option>
            <option>Rulemán</option>
            <option>Estopada</option
