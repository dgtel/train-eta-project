from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from your_ai_model import get_train_eta

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def home():
    return "Welcome to the Train ETA Backend! Use the '/get_eta' endpoint to get train ETA."

@app.route('/get_eta', methods=['POST'])
def calculate_eta():
    try:
        data = request.json
        train_data = data.get('train_data', '')
        if not train_data:
            return jsonify({"error": "Train data is required"}), 400
        eta = get_train_eta(train_data)
        return jsonify({"eta": eta})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
