from flask import Flask, render_template, render template

app = Flask(__name__)
@app.route("/")
def homepage():
    return ('Site de Mateus Vinicius da Silva padilha')

app.run()