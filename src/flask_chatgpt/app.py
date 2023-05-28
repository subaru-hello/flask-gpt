# src/flask_chatgpt/app.py

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    user_input = request.form.get('user_input')
    # Use LlamaIndex and ChatGPT with the user_input...
    return "Search results"

if __name__ == "__main__":
    app.run(debug=True)
