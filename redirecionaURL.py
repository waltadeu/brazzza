#! /usr/bin/python
# -*- coding: iso-8859-15 -*-

from flask import Flask, render_template, request, redirect
from flask_caching import Cache

cache = Cache(config={'CACHE_TYPE': 'null'})

app = Flask(__name__, template_folder='../pornobrx')

# defina a configuração do cache (isso pode ser feito em um arquivo de settings)
app.config["CACHE_TYPE"] = "null"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/termo', methods=['POST'])
def termo():
    return render_template('termo.html')

@app.route('/formulario', methods=['POST'])
def formulario():
    return render_template('form.html')

@app.route('/enviaFormulario', methods=['POST'])
def enviaFormulario():
    return render_template('/envia-form/envia.php')

@app.route('/banner', methods=['POST'])
def banner():
    return render_template('banner.html')

@app.route('/mudacategoria', methods=['POST'])
def mudaCategoria():
    name = request.form['categoria']
    genero = request.form['genero']
    return redirect("/"+genero+"/?categoria="+name+"/?1", code=302)

@app.route('/realizaBusca', methods=['POST'])
def realizaBusca():
    busca = request.form['campoBusca']
    campoGenero = request.form['campoGenero']
    return redirect("/?"+campoGenero+"/?busca="+busca+"/?1", code=302)

@app.route('/mudapagina', methods=['POST'])
def mudapagina():
    pagina = request.form['pagina']
    genero = request.form['genero']
    categoria = request.form['categoria']
    return redirect("/?"+genero+"/?categoria="+categoria+"/?"+pagina, code=302)

@app.route('/mudapaginaBusca', methods=['POST'])
def mudapaginaBusca():
    pagina = request.form['pagina']
    genero = request.form['genero']
    busca = request.form['busca']
    return redirect("/?"+genero+"/?busca="+busca+"/?"+pagina, code=302)

# AQUI VAMOS COLOCAR O ENDEREÇO DO NOSSO SITE
# ELE JÁ APONTA PARA O DIRETÓRIO TEMPLATE
if __name__ == '__main__':
    app.run(host='127.12.111.14')
