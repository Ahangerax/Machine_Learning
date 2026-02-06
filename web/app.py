from fastapi import FastAPI
import joblib
import numpy as np
import pandas as pd

app = FastAPI(title="House Price Prediction API")

model = joblib.load("model/housing_price_lgbm.pkl")


from pydantic import BaseModel

class HouseInput(BaseModel):
    longitude: float
    latitude: float
    housing_median_age: float
    total_rooms: float
    total_bedrooms: float
    population: float
    households: float
    median_income: float
    ocean_proximity: str


@app.post("/predict")
def predict_price(data: HouseInput):

    input_df = pd.DataFrame([data.dict()])

    log_prediction = model.predict(input_df)[0]
    price = np.exp(log_prediction)

    return {
        "predicted_house_price": round(float(price), 2)
    }
