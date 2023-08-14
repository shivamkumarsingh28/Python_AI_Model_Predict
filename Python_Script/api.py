import pickle
from BankNotes import BankNote
from fastapi import FastAPI 


# create fastapi app
app = FastAPI()

# Train model is classifier.pkl file load with help of pickle library
pickle_file =open("train_data/classifier.pkl","rb")
classifier = pickle.load(pickle_file)

# Index page only simple message print on screen
@app.get("/")
def index():
   return {"message": "Hello Python Bank Note Check Model"}

# welcome page take name parameter print on screen with welcome message  /api/welcome/{name}
@app.get("/api/welcome/{name}")
def welcome(name:str):
    return {f'Hello welcome to saeeam world - {name}'}

# Post method to take request to store in data variable as well as BankNote check input value is number not string and other thing
@app.post("/api/predict")
def predict_data(data: BankNote):
    data = data.dict()
    # print(data)
    variance = data['variance']
    skewness = data['skewness']
    curtosis = data['curtosis']
    entropy = data['entropy']

    # classifier variable machine model predict based on given value variance, skewness, curtosis, entropy output note real or fake.
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    if(prediction[0]>0.5):
        prediction = "Fake Note"
    else:
        prediction = "Its real note"

    return {
        'prediction': prediction
    }


# server serve on port 8000
if __name__ == '__main__':
   uvicorn.run(app)
