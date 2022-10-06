from flask import Flask, render_template, request, redirect

class Jogo:
    def __init__(self, nome, categoria, console, multiplayer):
        self.nome = nome
        self.categoria = categoria
        self.console = console
        self.multiplayer = multiplayer

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari', 'Não')
jogo2 = Jogo('God of War', 'Hack n Slash', 'PS2', 'Não')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2', 'Sim')
lista = [jogo1, jogo2, jogo3]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos que Pretendo Jogar', jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    multiplayer = request.form['multiplayer']
    jogo = Jogo(nome, categoria, console, multiplayer)
    lista.append(jogo)
    return redirect("/")

app.run(debug=True)