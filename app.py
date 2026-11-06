#Importar la libreria Flask
from flask import Flask, render_template
#Iniciar Flask
app = Flask(__name__)
#Creamos una ruta
@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/profe")
def profe():
    return "El negro y la Julia son los mejores profesores"

@app.route("/saludo/<nombre>")
def saludo(nombre):
    return f"Hola! {nombre}"

#Activamos el modo debug
if __name__ == "__main__":
    app.run(debug=True)