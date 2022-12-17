from flask import Flask

app = Flask(__name__)
# ruta pricicpal

@app.route('/')
def index():
    return "hola mundo"


if __name__ == '__main__':
    app.run(debug = True)