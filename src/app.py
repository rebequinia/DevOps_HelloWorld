from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

data = {
    "message": "Hello, World!"
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/api/message', methods=['GET'])
def get_message():
    return jsonify(data)

@app.route('/api/message', methods=['POST'])
def create_message():
    new_message = request.json.get('message')
    if not new_message:
        return jsonify({"error": "Missing 'message' field"}), 400
    data['message'] = new_message
    return jsonify({"message": "Message updated successfully", "new_message": data['message']}), 201

@app.route('/api/message', methods=['PUT'])
def update_message():
    updated_message = request.json.get('message')
    if not updated_message:
        return jsonify({"error": "Missing 'message' field"}), 400
    data['message'] = updated_message
    return jsonify({"message": "Message updated successfully", "new_message": data['message']})

@app.route('/api/message', methods=['DELETE'])
def delete_message():
    data['message'] = ''
    return jsonify({"message": "Message deleted"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
