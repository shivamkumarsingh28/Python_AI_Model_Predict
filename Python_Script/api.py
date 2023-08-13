import pickle
import pandas as pd
import numpy as np
from BankNotes import BankNote
from fastapi import FastAPI 


# create fastapi app
app = FastAPI()

pickle_file =open("train_data/classifier.pkl","rb")
classifier = pickle.load(pickle_file)

@app.get("/api/")
def index():
   return {"message": "Hello World"}

@app.get("/api/welcome/{name}")
def welcome(name:str):
    return {f'Hello welcome to saeeam world - {name}'}

@app.post("/api/predict")
def predict_data(data: BankNote):
    data = data.dict()
    variance = data['variance']
    skewness = data['skewness']
    curtosis = data['curtosis']
    entropy = data['entropy']

    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    if(prediction[0]>0.5):
        prediction = "Fake Note"
    else:
        prediction = "Its real note"

    return {
        'prediction': prediction
    }

if __name__ == '__main__':
   uvicorn.run(app, port='8000')