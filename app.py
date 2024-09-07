# app.py
from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)
current_expression = None

@app.route('/')
def index():
    with open('expression.txt', 'r') as file:
        current_expression = file.read().strip()
    return render_template('index.html', expression=current_expression)

@app.route('/get_expression')
def get_expression():
    global current_expression
    with open('expression.txt', 'r') as file:
        new_expression = file.read().strip()
    
    if new_expression != current_expression:
        current_expression = new_expression
        return jsonify({'changed': True, 'expression': current_expression})
    return jsonify({'changed': False})

@app.route('/svg/<expression>')
def get_svg(expression):
    with open(f'static/images/{expression}-robot-eyes.svg', 'r') as file:
        svg_content = file.read()
    return svg_content, 200, {'Content-Type': 'image/svg+xml'}

if __name__ == '__main__':
    app.run(debug=True)
