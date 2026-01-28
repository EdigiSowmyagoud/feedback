from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

feedback_list = []

# Serve index.html
@app.route('/')
def serve_index():
    return send_from_directory('../frontend', 'index.html')

# Serve other frontend files (JS/CSS)
@app.route('/<path:path>')
def serve_frontend(path):
    return send_from_directory('../frontend', path)

@app.route('/feedback', methods=['POST'])
def submit_feedback():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    if not name or not message:
        return jsonify({"error": "Name and message are required"}), 400

    feedback_list.append({"name": name, "email": email, "message": message})
    print("New Feedback:", feedback_list[-1])
    return jsonify({"message": "Feedback received!"}), 200

@app.route('/all-feedback', methods=['GET'])
def get_feedback():
    return jsonify(feedback_list)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
