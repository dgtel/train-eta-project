import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split

# Load the dataset
data = pd.read_csv('../data/train_eta_data.csv')

# Print the first few rows of the dataset
print("Dataset Preview:")
print(data.head())

# Extract features (Distance, Speed) and target (ETA)
X = data[['Distance', 'Speed']].values
y = data['ETA'].values

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the model
model = Sequential([
    Dense(16, input_dim=2, activation='relu'),  # Input layer (2 features)
    Dense(8, activation='relu'),               # Hidden layer
    Dense(1, activation='linear')              # Output layer (ETA)
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])

# Train the model
model.fit(X_train, y_train, epochs=100, batch_size=4, verbose=1)

# Evaluate the model
loss, mae = model.evaluate(X_test, y_test, verbose=0)
print(f"Test Loss: {loss}, Test MAE: {mae}")

# Save the trained model
model.save('../data/train_eta_model.h5')
print("Model saved as 'train_eta_model.h5' in the data folder.")
