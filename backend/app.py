from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from your_ai_model import get_train_eta

from flask import redirect

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def home():
    return redirect("https://dgtel.github.io/train-eta-project/frontend/train_eta.html")

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

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Default to 5000 if PORT is not set
    app.run(host='0.0.0.0', port=port)

