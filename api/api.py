import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '''<h1>API Prueba Flask-Python</h1>
<p>Este es un demo de api con Flask</p>'''


@app.route('/api/v1/suma', methods=['POST'])
def api_all():
    datos = request.get_json()
    num_1 = datos["num1"]
    num_2 = datos["num2"]
    suma = {"respuesta": num_1 + num_2}
    return jsonify(suma)

app.run()

