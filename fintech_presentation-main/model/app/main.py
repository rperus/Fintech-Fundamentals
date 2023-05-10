from fastapi import FastAPI
import pickle
from sklearn.pipeline import Pipeline
import pandas as pd
import uvicorn
from pydantic import BaseModel


class LoanApplication(BaseModel):
    """
    Loan Application Data Schema
    """
    loan_amnt: float
    term: int
    emp_length: int
    annual_inc: float

class CreditRiskScore(BaseModel):
    """
    Credit Risk Score data schema
    """

    credit_risk_score: float

app = FastAPI()

# load model (sklearn pipeline)
model = pickle.load(
    open('app/model.pkl', 'rb')
)

@app.get('/')
def read_root():
    """
    Display welcome message
    """

    return {"message": "Welcome to Machine Learning Model API"}

@app.post('/predict/', response_model=CreditRiskScore)
def get_prediction(payload: LoanApplication):
    """
    Return model prediction given inputs.
    Inputs:
    ========
    payload (str): variables used to compute prediction

    Outputs:
    ========
    {'prediction': prediction (float)}:
    score from 0 to 1. Closer to 1 is better
    """

    input_ = pd.DataFrame(payload.dict(),[0])
    
    # take first element
    prediction = model.predict_proba(input_)[:, 1][0]

    score = CreditRiskScore(credit_risk_score=prediction)

    return score

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=1111)