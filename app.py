from flask import Flask, request

app = Flask(__name__)

registros = []

@app.route("/")
def inicio():

    html = """
    <h1>SGM Bombas SVE v1.0</h1>

    <a href='/nuevoRegistrar mantenimiento
    </a>

    <br><br>

    /historial
        Ver historial
    </a>
    """

    return html


@app.route("/nuevo", methods=["GET", "POST"])
def nuevo():

    if request.method == "POST":

        bomba = request.form["bomba"]
        componente = request.form["componente"]
        observacion = request.form["observacion"]

        registros.append({
            "bomba": bomba,
            "componente": componente,
            "observacion": observacion
        })

        return """
        <h2>Registro guardado</h2>

        /
        Volver
        </a>
        """

    bombas = ""

    for i in range(1, 24):
        bombas += f"<option>C{i}</option>"

    return f"""
    <h1>Nuevo mantenimiento</h1>

    <form method='post'>

        <label>Bomba</label>

        <select name='bomba'>
            {bombas}
        </select>

        <br><br>

        <label>Componente</label>

        <select name='componente'>

            <option>Comando eléctrico</option>
            <option>Cable y enchufe</option>
            <option>Motor</option>
            <option>Turbina</option>
            <option>Cabezal</option>
            <option>Rulemán</option>
            <option>Estopada</option>
            <option>Pintado</option>
            <option>Ruedas</option>

        </select>

        <br><br>

        <textarea
            name='observacion'
            placeholder='Observaciones'
        ></textarea>

        <br><br>

        <button>
            Guardar
        </button>

    </form>
    """


@app.route("/historial")
def historial():

    html = "<h1>Historial</h1>"

    for r in registros:

        html += f"""
        <p>
        {r['bomba']} -
        {r['componente']} -
        {r['observacion']}
        </p>
        """

    html += "<br>/Volver</a>"

    return html


if __name__ == "__main__":
    app.run()
