# app.py
from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

@app.route("/")
def index():
    # Display a simple page that shows app version and environment
    version = os.environ.get("APP_VERSION", "0.1.0")
    env = os.environ.get("APP_ENV", "development")
    return render_template("index.html", version=version, env=env)

@app.route("/health")
def health():
    return jsonify(status="ok", version=os.environ.get("APP_VERSION", "0.1.0"))

if __name__ == "__main__":
    # Use environment variables for host/port when running in container/CI
    host = os.environ.get("FLASK_RUN_HOST", "0.0.0.0")
    port = int(os.environ.get("FLASK_RUN_PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "1") == "1"
    app.run(host=host, port=port, debug=debug)
