from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

# Helper function to get the current expression from the file
def get_current_expression():
    with open('expression.txt', 'r') as file:
        return file.read().strip()

# Helper function to read from 'speak_me.txt' and clear the file
def check_and_clear_speech_file():
    file_path = 'speak_me.txt'
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            content = file.read().strip()
        
        # Clear the contents of the file
        with open(file_path, 'w') as file:
            file.write('')
            
        return content
    else:
        return ""  # Return empty string if the file doesn't exist

@app.route('/')
def index():
    current_expression = get_current_expression()
    return render_template('index.html', expression=current_expression)

@app.route('/get_expression')
def get_expression():
    current_expression = get_current_expression()
    return current_expression
    
@app.route('/svg/<expression>')
def get_svg(expression):
    svg_path = f'static/images/{expression}-robot-eyes.svg'
    if os.path.exists(svg_path):
        with open(svg_path, 'r') as file:
            svg_content = file.read()
        return svg_content, 200, {'Content-Type': 'image/svg+xml'}
    return "SVG not found", 404

@app.route('/check_speech')
def check_speech():
    speech_content = check_and_clear_speech_file()
    return speech_content

if __name__ == '__main__':
    app.run(debug=True)
