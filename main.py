from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "API is running."}

@app.post("/predict")
async def predict():
    return {"message": "Predict route works."}
