from flask import Blueprint, jsonify

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return jsonify({"message": "Hello from Flask CI/CD app!", "status": "ok"})

@main.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200