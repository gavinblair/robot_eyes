from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)
previous_expression = None

def get_current_expression():
    with open('expression.txt', 'r') as file:
        return file.read().strip()

@app.route('/')
def index():
    current_expression = get_current_expression()
    return render_template('index.html', expression=current_expression)

@app.route('/get_expression')
def get_expression():
    global previous_expression
    current_expression = get_current_expression()

    if current_expression != previous_expression:
        previous_expression = current_expression
        return jsonify({'changed': True, 'expression': current_expression})

    return jsonify({'changed': False})

@app.route('/svg/<expression>')
def get_svg(expression):
    svg_path = f'static/images/{expression}-robot-eyes.svg'
    if os.path.exists(svg_path):
        with open(svg_path, 'r') as file:
            svg_content = file.read()
        return svg_content, 200, {'Content-Type': 'image/svg+xml'}
    return "SVG not found", 404

if __name__ == '__main__':
    app.run(debug=True)
