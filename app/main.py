from fastapi import FastAPI
from app.model.prework import work
import uvicorn

# initilizing app
app = FastAPI()

@app.get('/')
async def home():
    return{"text" : "Hello smth"}


@app.post("/predict")
def predict(payload):
    type_of_incident = work(payload.text)
    return {"the type is ": type_of_incident}

# if __name__ == '__main__':
#     uvicorn.run(app, host="127.0.0.1", port=8000)
