from fastapi import FastAPI
from locale import atof, setlocale, LC_NUMERIC
import requests
from utils import coindesk_btc_fiat, get_sats_amt

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:5000",
    "http://localhost:8000",
]


@app.get("/")
def Home():
    return 'SatsPay Session!'


@app.get('/about')
def about():
    return 'About'

# @app.route('/<fiat>')
# def dynamic_endpoint(fiat):
#     amount = requests.args.get('amount')  
#     if amount:
#         content =  f"Endpoint for {fiat}, The amount is: {amount}"
#         sats = get_sats_amt(amount, fiat)
#         content += f"Sats amount: {sats}"
#         return content
#     else:
#         return f"Endpoint for {fiat}, No amount provided."
