from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <h1>SGM Bombas SVE v1.0</h1>

    <p>✅ Aplicación funcionando</p>

    <p>
        /nuevo🛠 Registrar mantenimiento</a>
    </p>

    <p>
        /historial📋 Ver historial</a>
    </p>
    """

@app.route("/nuevo")
def nuevo():
    return """
    <h1>Nuevo mantenimiento</h1>

    <p>Pantalla en construcción</p>

    /Volver</a>
    """

@app.route("/historial")
def historial():
    return """
    <h1>Historial</h1>

    <p>Historial en construcción</p>

    /Volver</a>
    """

if __name__ == "__main__":
    app.run()
