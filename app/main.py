from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "dev")


@app.route("/")
def index():
    return jsonify(
        {
            "message": "Hello from the GitOps demo app!",
            "version": APP_VERSION,
            "hostname": socket.gethostname(),
        }
    )


@app.route("/healthz")
def healthz():
    """Liveness/readiness probe endpoint used by Kubernetes."""
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
