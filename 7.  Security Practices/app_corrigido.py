from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False) # Comprimento de 128 para armazenar o hash

# Criei também esse endpoint para cadastrar novos usuários
@app.route('/create_user', methods=['POST'])
def create_user():
    username = request.form['username']
    password = request.form['password']

    # Verifica se o usuário inserido já não existe
    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'User already exists'}), 400

    password_hash = generate_password_hash(password)
    new_user = User(username=username, password_hash=password_hash)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created'}), 201


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username).first()

    # Verifica se o hash da senha digitada corresponde ao armazenado
    if user and check_password_hash(user.password_hash, password):
        return jsonify({'message': 'Acesso concedido'}), 200

    return jsonify({'message': 'Acesso negado'}), 401

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=False)  
