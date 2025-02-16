from flask import Flask, request
app = Flask(__name__)
 
@app.route('/login', methods=['POST'])
def login():
	username = request.form['username']
	password = request.form['password']
	if username == 'admin' and password == '1234':
        return "Acesso concedido"
	return "Acesso negado"
 
if __name__ == '__main__':
    app.run(debug=True)

''' Erros notados
1 - Não possui nenhum banco de dados para armazenar os dados de login,
da forma como está o código teria que fazer um if para cada usuário, o que 
seria extremamente inviável e não seguro.

2 - Não possui nenhuma função hash para a senha, o que deixa a senha exposta no código
'''