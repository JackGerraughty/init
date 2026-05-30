from flask import Flask, render_template, send_from_directory
import os
import serverless_wsgi

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))
    app.run(host="0.0.0.0", port=port)