from flask import Flask, render_template, request, redirect
lista = []

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('Home.html', Titulo='Bem-vindo ao site de Café')

@app.route('/sobre')
def sobre():
    return render_template('Sobre.html', Titulo='Sobre o nosso site')

@app.route('/cadastro')
def cadastro():
    return render_template('Cadastro.html', Titulo='Cadastro de Cafés')

@app.route('/exibir')
def exibir():
    return render_template('Exibir.html', Titulo='Cafés cadastrados', lista=lista)

@app.route('/cafe')
def cafe():
    return render_template('Cafe.html', Titulo='Exemplos café')

@app.route('/contato')
def contato():
    return render_template('Contato.html', Titulo='Contatos')

@app.route('/criar', methods=['POST'])
def criar():
    numero = request.form['numero']
    marca = request.form['marca']
    tipo = request.form['tipo']
    peso = request.form['peso']
    cafe = [marca, tipo, peso, numero]
    lista.append(cafe)
    return redirect('/exibir')