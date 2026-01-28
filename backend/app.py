from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for feedback (no database needed)
feedback_list = []

@app.route('/')
def home():
    return "User Feedback Backend Running!"

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
    # Returns all feedback
    return jsonify(feedback_list)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)


