import os
from flask import Flask, jsonify

app = Flask(__name__)

BUILD = "build-2-by-claude"

@app.route("/")
def hello_world():
    return f"<p>Hello, World! Webhook!!! demo1-1!! {BUILD}</p>"

@app.route("/health")
def health():
    return jsonify(status="ok", build=BUILD), 200

if __name__ == '__main__':
    port = int(os.getenv("PORT", 8081))
    debug = os.getenv("DEBUG", "false").lower() == "true"
    app.run(host="0.0.0.0", port=port, debug=debug)
