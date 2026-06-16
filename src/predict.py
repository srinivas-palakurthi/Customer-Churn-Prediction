import joblib
import pandas as pd

model = joblib.load("model.pkl")

def predict_customer(data):

    df = pd.DataFrame([data])

    prediction = model.predict(df)

    return prediction[0]
