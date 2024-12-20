import os
from tensorflow.keras.models import load_model
import numpy as np

# Get the absolute path to the model
model_path = os.path.join(os.path.dirname(__file__), '../data/train_eta_model.h5')
model = load_model(model_path)

def get_train_eta(train_data):
    try:
        # Parse the input data (distance and speed)
        distance, speed = map(float, train_data.split(','))  # Example input: "200,50"
        features = np.array([distance, speed]).reshape(1, -1)
        
        # Predict ETA using the model
        eta = model.predict(features)[0][0]
        return f"{eta:.2f} hours"
    except Exception as e:
        return f"Error processing train data: {str(e)}"

