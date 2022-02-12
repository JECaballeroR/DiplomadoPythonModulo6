from fastapi import  FastAPI
from typing import  List
from classes import ModelInput, ModelOutput, APIModelBackEnd


app = FastAPI(title="API de Machine Learning del Diplomado")

@app.post("/predict", response_model=List[ModelOutput])
async def predict_proba(Inputs: List[ModelInput]):
    response = []
    for Input in Inputs:
        Model = APIModelBackEnd(Input.satisfaction_level, Input.average_montly_hours, Input.salary_level)
        response.append(Model.predict()[0])

    return response