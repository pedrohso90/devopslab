from flask import Flask
import os

app = Flask(__name__)

port = int(os.environ.get("PORT", 5000))

@app.route("/")
def pagina_inicial():
    return "Hello World"

@app.route("/soma")
def soma_valores():
    x=10+10
    return "Sua soma de 10+10="+str(x)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
