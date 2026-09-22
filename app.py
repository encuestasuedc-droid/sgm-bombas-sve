from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def inicio():
return """
<h1>SGM Bombas SVE v1.0</h1>
<h3>Sistema de Gestión de Mantenimiento</h3>
 
<ul>
<li>C1 a C23</li>
<li>Registro de reparaciones</li>
<li>Historial</li>
<li>Dashboard</li>
</ul>
"""
 
if __name__ == "__main__":
app.run()
