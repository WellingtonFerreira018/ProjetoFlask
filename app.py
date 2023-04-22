from flask import Flask, render_template, request
import urllib.request
import json

app = Flask(__name__)

frutas = []
registros = []


@app.route('/', methods=["GET", "POST"])
def principal():
    if request.method == "POST":
        if request.form.get("fruta"):
            frutas.append(request.form.get("fruta"))

    return render_template("index.html", frutas=frutas)


@app.route('/sobre', methods=["GET", "POST"])
def sobre():
    if request.method == "POST":
        if request.form.get("aluno") and request.form.get("nota"):
            registros.append({"Aluno": request.form.get(
                "aluno"), "Nota": request.form.get("nota")})

    return render_template('sobre.html', registros=registros)


@app.route('/filmes/<propriedade>')
def filmes(propriedade):
    
    if propriedade == 'populares':
        url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=29fb891b5bbaeba61c7e6aa498be7d9e"
    elif propriedade == 'kids':
        url = "https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key=29fb891b5bbaeba61c7e6aa498be7d9e"
    elif propriedade == '2010':
        url = "https://api.themoviedb.org/3/discover/movie?primary_release_year=2010&sort_by=vote_average.desc&api_key=29fb891b5bbaeba61c7e6aa498be7d9e"
    elif propriedade == 'drama':
        url = "https://api.themoviedb.org/3/discover/movie?with_genres=18&sort_by=vote_average.desc&vote_count.gte=10&api_key=29fb891b5bbaeba61c7e6aa498be7d9e"
    elif propriedade == 'ton_cruise':
        url = "https://api.themoviedb.org/3/discover/movie?with_genres=878&with_cast=500&sort_by=vote_average.desc&api_key=29fb891b5bbaeba61c7e6aa498be7d9e"
    
    
    resposta = urllib.request.urlopen(url)
    dados = resposta.read()

    jsonData = json.loads(dados)

    return render_template('filmes.html', filmes=jsonData['results'])


if __name__ == "__main__":
    app.run(debug=True)
