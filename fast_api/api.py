from fastapi import FastAPI

app = FastAPI()

# define a root '/' endpoint


# Each one of the below is an endpoint!
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
    # REMEMBER that the parameters passed above are of type str. So don't
    # forget to consider this and convert to numerical datatype (as below).
    wait_prediction = int(day_of_week) - 2*.8  #just an example
    return {'wait': wait_prediction}
