from flask import Flask, render_template, abort

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/suma/<int:a>/<int:b>")
def suma(a, b):
    return f"{a} + {b} = {a + b}, <a href = '/'>Volver</a>"


@app.route("/resta/<int:a>/<int:b>")
def resta(a, b):
    return f"{a} - {b} = {a - b}, <a href = '/'>Volver</a>"

@app.route("/multiplicacion/<int:a>/<int:b>")
def multiplicacion(a, b):
    return f"{a} * {b} = {a * b}, <a href = '/'>Volver</a>"

@app.route("/division/<int:a>/<int:b>")
def division(a, b):
    if b == 0 or a == 0:
        return f"Error, no se puede dividir entre cero, <a href ='/'>Volver</a>"
    return f"{a} / {b} = {a / b}"

@app.errorhandler(404)
def no_encontrado(error):
    return f"<h1>404</h1><p>Esa ruta no existe</p1><a href ='/'>Volver</a>", 404

@app.errorhandler(400)
def peticion_invalida(error):
    return f"<h1>400</h1><p>{error.description}</p><a href='/'>Volver</a>", 400

if __name__ == "__main__":
    app.run(debug=True, port=5000)