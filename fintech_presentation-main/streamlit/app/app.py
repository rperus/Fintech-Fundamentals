import datetime
import streamlit as st
import requests
from sqlalchemy import create_engine
from sqlalchemy.types import JSON
import pandas as pd

st.title("Jack's Fintech")
st.write("## Apply for a Loan by Filling the Application Below")

loan_amnt = st.text_input("Enter Loan Amount", 10)
term = st.selectbox("Choose Loan Terms", (36, 60))
emp_length = st.selectbox(
    "How long have you been employed?",
    (10, 2, 0, 3, 1, 5, 4, 6, 8, 7, 9)    
)
annual_inc = st.text_input("Enter your Annual Income", 10)

data = {
    "loan_amnt": float(loan_amnt),
    "term": term,
    "emp_length": emp_length,
    "annual_inc": float(annual_inc)
}

st.write("You have entered:")
st.json(data)

if st.button("Apply for the Loan!"):
    res = requests.post(
        "http://model:1111/predict",
        json=data
    )
    score = res.json()
    
    st.write("Your Score:")
    st.json(score)

    # write to postgres database
    to_db = pd.DataFrame()
    to_db['request'] = [data]
    to_db['response'] = score

    to_db.index = [datetime.datetime.now()]
    to_db.index.name = 'datestamp'

    # Do not store connection string in the code!
    db_engine = create_engine(
        "postgresql://root:change_me@postgres:5432/postgres"
    )

    to_db.to_sql(
        "fintech_data",
        db_engine,
        if_exists='append',
        index=True,
        dtype={'request': JSON, 'response': JSON}
    )