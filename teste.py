import urllib.request, json

url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=29fb891b5bbaeba61c7e6aa498be7d9e"

resposta = urllib.request.urlopen(url)

dados = resposta.read()

jsonData = json.loads(dados)

print(jsonData['results'])
