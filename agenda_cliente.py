from flask import Flask, render_template, request, redirect, session, flash, url_for

class Paciente:
    def __init__(self, nome, especialidade, horario, telefone):
        self.nome=nome
        self.especialidade=especialidade
        self.horario=horario
        self.telefone=telefone

paciente1 = Paciente('Douglas Silva', 'Ortopedista', '09:30', '98984678990')
paciente2 = Paciente('Renata Sousa', 'Clínico Geral', '10:30', '9832239090')
paciente3 = Paciente('Cristina Pereira', 'Genética', '11:30', '98991999021')
lista = [paciente1, paciente2, paciente3]

class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha

usuario1 = Usuario("Jorge Lago", "lagojorge", "senha123")
usuario2 = Usuario("Bruna Surama", "surama", "123senha")

usuarios = { usuario1.nickname : usuario1,
             usuario2.nickname : usuario2 }

app = Flask(__name__)
app.secret_key = 'consultorio'

@app.route('/')
def index():
    return render_template('lista.html', titulo='Paciente', paciente=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Paciente')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    especialidade = request.form['especialidade']
    horario = request.form['horario']
    telefone = request.form['telefone']
    paciente = Paciente(nome, especialidade, horario, telefone)
    lista.append(paciente)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ' logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Usuário não logado.')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))

app.run(debug=True)