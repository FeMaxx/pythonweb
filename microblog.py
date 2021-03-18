from flask import Flask

app = Flask ("microbog")

#função para rota (localhost:5000)
@app.route("/")
def index():
    return "Olá Mundo"

app.run()