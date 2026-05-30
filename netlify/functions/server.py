from flask import Flask, render_template, send_from_directory
import os
import serverless_wsgi

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../..")
)

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)

@app.route("/")
def index():
    return render_template("congrats.html")

@app.route("/example")
def example():
    return send_from_directory(
        os.path.join(BASE_DIR, "static"),
        "example.py"
    )

def handler(event, context):
    return serverless_wsgi.handle_request(app, event, context)