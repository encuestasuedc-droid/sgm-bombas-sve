from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bombas.db"

db = SQLAlchemy(app)

class Mantenimiento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bomba = db.Column(db.String(20))

with app.app_context():
    db.create_all()

@app.route("/")
def inicio():
    return """
    <h1>SGM Bombas SVE v1.0</h1>
    <p>✅ SQLite funcionando</p>
    """

if __name__ == "__main__":
    app.run()
