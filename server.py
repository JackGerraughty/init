import os
import socket
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
HOST = "::"
PORT = int(os.environ.get("PORT", "8080"))


class DualStackHTTPServer(ThreadingHTTPServer):
    address_family = socket.AF_INET6


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in ("/", "/index.html"):
            self.send_html(
                """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Railway Python Server</title>
  <style>
    body {
      margin: 0;
      min-height: 100vh;
      display: grid;
      place-items: center;
      font-family: Arial, sans-serif;
      background: #f6f7f9;
      color: #1f2937;
    }
    main {
      width: min(560px, calc(100vw - 40px));
      padding: 28px;
      border: 1px solid #d7dce2;
      border-radius: 8px;
      background: #fff;
    }
    h1 { margin: 0 0 12px; font-size: 28px; }
    p { margin: 0 0 18px; line-height: 1.5; }
    a { color: #0f62fe; }
  </style>
</head>
<body>
  <main>
    <h1>Python server is running</h1>
    <p>This is a basic Railway-ready Python server using only the standard library.</p>
    <a href="/health">Health check</a>
  </main>
</body>
</html>"""
            )
            return

        if self.path == "/health":
            self.send_text("ok\n")
            return

        if self.path == "/example":
            example_path = BASE_DIR / "static" / "example.py"
            self.send_text(example_path.read_text(encoding="utf-8"))
            return

        if self.path == "/favicon.ico":
            self.send_response(204)
            self.end_headers()
            return

        self.send_text("not found\n", status=404)

    def log_message(self, format, *args):
        print("%s - %s" % (self.address_string(), format % args), flush=True)

    def send_html(self, body, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body.encode("utf-8"))))
        self.end_headers()
        self.wfile.write(body.encode("utf-8"))

    def send_text(self, body, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body.encode("utf-8"))))
        self.end_headers()
        self.wfile.write(body.encode("utf-8"))


if __name__ == "__main__":
    print(f"Starting server on {HOST}:{PORT}", flush=True)
    DualStackHTTPServer((HOST, PORT), Handler).serve_forever()
