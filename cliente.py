from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return "¡Hola, mundo!"


@app.route("/saludar", methods=["POST"])
def saludar():
    nombre = request.json.get("nombre")
    return f"Hola, {nombre}!"


if __name__ == "__main__":
    app.run()
