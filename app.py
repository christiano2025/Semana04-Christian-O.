from flask import Flask, request, render_template

app = Flask(__name__)

comentarios = []

@app.route("/")
def inicio():
    return render_template("comentarios.html", comentarios=comentarios)

@app.route("/comentario", methods=["POST"])
def comentario():
    mensaje = request.form["mensaje"]

    if len(mensaje) > 200:
        return "Comentario demasiado largo"

    comentarios.append(mensaje)

    return render_template("comentarios.html", comentarios=comentarios)

if __name__ == "__main__":
    app.run(debug=True)