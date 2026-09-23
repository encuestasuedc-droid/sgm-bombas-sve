from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/nuevo")
def nuevo():
    return render_template("registro.html")

@app.route("/historial")
def historial():
    return render_template("historial.html")

if __name__ == "__main__":
    app.run()
