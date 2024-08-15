from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/teste', methods=['GET'])
def teste():
    return 'hello'

@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.get_json()
    valor1 = data.get('valor1').replace(',', '.')
    valor2 = data.get('valor2').replace(',', '.')
    try:
        resultado = float(valor1) + float(valor2)
        return jsonify({'resultado': resultado})
    except ValueError:
        return jsonify({'resultado': 'Valores inválidos'})

if __name__ == '__main__':
    app.run(debug=True)




