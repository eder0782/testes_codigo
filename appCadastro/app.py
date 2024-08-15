from flask import Flask, request, jsonify, render_template
import sqlite3 as sq

app = Flask(__name__)

def get_db_connection():
    con = sq.connect('database.db')
    con.row_factory = sq.Row
    return con

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/listar', methods=['GET'])
def listar():
    con = get_db_connection()
    cursor = con.execute('SELECT * FROM USUARIO')
    usuarios = cursor.fetchall()
    con.close()
    return jsonify([dict(ix) for ix in usuarios])

@app.route('/salvar', methods=['POST'])
def salvar():
    data = request.get_json()
    id = data['id']
    nome = data['nome']
    try:
        con = get_db_connection()
        con.execute('INSERT INTO USUARIO (ID, NOME) VALUES (?, ?)', (id, nome))
        con.commit()
        con.close()
        return jsonify({'message': 'Registro salvo com sucesso!'})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/update', methods=['POST'])
def update():
    data = request.get_json()
    id = data['id']
    nome = data['nome']
    try:
        con = get_db_connection()
        con.execute('UPDATE USUARIO SET NOME = ? WHERE ID = ?', (nome, id))
        con.commit()
        con.close()
        return jsonify({'message': 'Registro atualizado com sucesso!'})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/deletar', methods=['POST'])
def deletar():
    data = request.get_json()
    id = data['id']
    try:
        con = get_db_connection()
        con.execute('DELETE FROM USUARIO WHERE ID = ?', (id,))
        con.commit()
        con.close()
        return jsonify({'message': 'Registro excluído com sucesso!'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

