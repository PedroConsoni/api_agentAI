from flask import Flask, render_template, request, redirect, session, url_for, jsonify
from auth import verificar_login
from agent import root_agent

app = Flask(__name__)
app.secret_key ="chave123456789"

@app.route("/")
def home():
    if "usuario" not in session:
        return redirect(url_for("login"))
    return render_template("home.html", usuario=session["usuario"])

@app.route("/login", methods=["GET", "POST"])
def login():
    erro = None

    if request.method == "POST":
        usuario = request.form.get("usuario")
        senha = request.form.get("senha")

        if verificar_login(usuario, senha):
            session["usuario"] = usuario
            return redirect(url_for("home"))
        else:
            erro = "Usuário ou senha incorretos!"

    return render_template("login.html", erro=erro)

@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
