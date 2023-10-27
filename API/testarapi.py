import requests

link = "http://127.0.0.1:5000/Valor Final"

requisicao = requests.get(link)

print(requisicao.json())
