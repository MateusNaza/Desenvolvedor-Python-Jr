from flask import Flask, request, jsonify

app = Flask(__name__)

# Definição do endpoit 'GET /saudacao?nome=SeuNome'
@app.route('/saudacao', methods=['GET'])
def saudacao():
    nome = request.args.get('nome', 'Amigo')
    return f'Olá, {nome}! Muito feliz em te ver por aqui! :)'

# Definição do endpoit 'POST /soma'
@app.route('/soma', methods=['POST'])
def soma():
    dados = request.get_json()
    num1 = dados.get('num1', 0)
    num2 = dados.get('num2', 0)
    resultado = num1 + num2
    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run()