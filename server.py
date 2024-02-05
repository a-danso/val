from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/submit_answer", methods=['POST', 'GET'])
def submit_answer():
    if request.method == 'POST':
        return render_template('gratitude.html')