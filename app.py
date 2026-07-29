from flask import Flask, jsonify
from calculator import add, subtract, multiply, divide

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({'status': 'ok', 'service': 'calculator-api'})

@app.route('/add/<int:a>/<int:b>')
def add_route(a, b):
    return jsonify({'result': add(a, b)})

@app.route('/subtract/<int:a>/<int:b>')
def subtract_route(a, b):
    return jsonify({'result': subtract(a, b)})

@app.route('/multiply/<int:a>/<int:b>')
def multiply_route(a, b):
    return jsonify({'result': multiply(a, b)})

@app.route('/divide/<int:a>/<int:b>')
def divide_route(a, b):
    try:
        return jsonify({'result': divide(a, b)})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
