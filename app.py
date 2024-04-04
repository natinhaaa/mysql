from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configuração do banco de dados
db = mysql.connector.connect(
    host="127.0.0.1",
    user="user",
    password="123",
    database="Users"
)

cursor = db.cursor()

# Rota para a página de login
@app.route('/')
def login():
    return render_template('login.html')

# Rota para lidar com o processo de login
@app.route('/login', methods=['POST'])
def login_post():
    login = request.form['username']
    senha = request.form['password']

    cursor.execute("select * from Usuarios WHERE Login = %s AND Senha = %s", (login, senha))
    user = cursor.fetchone()

    if user:
        return render_template('usuarios.html', usuario=login)
    else:
        mensagem = "Usuário ou senha incorretos. Tente novamente."
        return render_template('login.html', mensagem=mensagem)

if __name__ == '__main__':
    app.run(debug=True)