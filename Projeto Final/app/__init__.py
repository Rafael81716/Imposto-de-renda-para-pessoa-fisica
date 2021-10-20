from flask import Flask
app = Flask(__name__)
#Esse comando vai criar um codigo que define um nome a um arquivo, podendo ser principal ou secundario

from app.controllers import routes