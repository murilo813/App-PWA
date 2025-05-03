from flask import Flask, render_template
from functions import buscar_estoque

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/bela_vista")
def bela_vista():
    dados = buscar_estoque("estoque_belavista")
    return render_template("bela_vista.html", titulo="Bela Vista", dados=dados)

@app.route("/imbuia")
def imbuia():
    dados = buscar_estoque("estoque_imbuia")
    return render_template("imbuia.html", titulo="Imbuia", dados=dados)

@app.route("/vila_nova")
def vila_nova():
    dados = buscar_estoque("estoque_vilanova")
    return render_template("vila_nova.html", titulo="Vila Nova", dados=dados)

@app.route("/aurora")
def aurora():
    dados = buscar_estoque("estoque_aurora")
    return render_template("aurora.html", titulo="Aurora", dados=dados)

@app.route("/logout")
def logout():
    return render_template("logout.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
