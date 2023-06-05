from fastapi import FastAPI

app = FastAPI()

# define a root '/' endpoint

@app.get("/")

def index():
    # Here you can load a machine learning model
    # You can also do a prediction model.predict(...)
    return {'ok': True}


@app.get("/predict")

# what if you want to pass parameters to the endpoint?
# You just need to define the parameters you want to pass as
# the function parameters

def predict(day_of_week):
    # REMEMBER that the parameters passed above are of type str
    # so don't forget to consider this and convert to numerical datatype.
    wait_prediction = int(day_of_week) - 2*.8  #just an example
    return {'wait': wait_prediction}
