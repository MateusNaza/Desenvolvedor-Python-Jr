import requests
import json

# Abrindo o arquivo para leitura
with open('numbers_for_sum.json', 'r') as file:
    data = json.load(file)

# URL do ambiente local, onde esta rodando o código com o endpoint /soma ao final da URL
url = 'http://127.0.0.1:5000/soma'
headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=json.dumps(data), headers=headers)

print(response.json())
