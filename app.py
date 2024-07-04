from flask import Flask
from flask import jsonify
from componentes.consultar import traer_todos

app = Flask(__name__)



@app.route('/')
def inicio():
    return "Bienvenidos a Flask"
app.route('/')


@app.route('/api/todos')
def mostrar():
    contenido =traer_todos()
    return jsonify(contenido)

if __name__ == '__main__':
    app.run(debug=True)