from flask import Flask, request
import boto3, uuid

app = Flask(__name__)
table = boto3.resource('dynamodb').Table('feedback')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    data['id'] = str(uuid.uuid4())
    table.put_item(Item=data)
    return {"status": "success"}

app.run(host='0.0.0.0', port=5000)

