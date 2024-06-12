import joblib
import numpy as np

def preprocess(Open, High, Low, Volume):
    # Convert input data to numeric values
    Open = float(Open)
    High = float(High)
    Low = float(Low)
    Volume = float(Volume)

    # Create a 1D array
    input_data = np.array([Open, High, Low, Volume])

    # Reshape the 1D array into a 2D array
    input_data_2d = input_data.reshape(1, -1)

    trained_model = joblib.load("model.pkl")
    
    prediction = trained_model.predict(input_data_2d)

    return prediction
