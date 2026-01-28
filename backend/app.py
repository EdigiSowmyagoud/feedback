from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

FEEDBACK_LIST = []

# Serve index.html from frontend folder
@app.route('/')
def serve_index():
    return send_from_directory('../frontend', 'index.html')

# Serve other frontend files (JS/CSS)
@app.route('/<path:path>')
def serve_frontend(path):
    return send_from_directory('../frontend', path)

# Feedback POST
@app.route('/feedback', methods=['POST'])
def submit_feedback():
    data = request.get_json()
    name = data.get('name')
    message = data.get('message')
    email = data.get('email', '')

    if not name or not message:
        return jsonify({"error": "Name and message required"}), 400

    FEEDBACK_LIST.append({"name": name, "email": email, "message": message})
    print("New Feedback:", FEEDBACK_LIST[-1])
    return jsonify({"message": "Feedback received!"}), 200

# Return all feedback
@app.route('/all-feedback', methods=['GET'])
def get_feedback():
    return jsonify(FEEDBACK_LIST)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
