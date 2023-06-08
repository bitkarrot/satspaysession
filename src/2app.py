from flask import Flask
from locale import atof, setlocale, LC_NUMERIC
import requests
import uvicorn

app = Flask(__name__)

def coindesk_btc_fiat(symbol):
    # batch the requests together via asyncio or multiprocessing
    setlocale(LC_NUMERIC, '')
    url = f'https://api.coindesk.com/v1/bpi/currentprice/{symbol}.json'
    response = requests.get(url)
    ticker = response.json()
    time = ticker["time"]['updated']
    rate = ticker['bpi'][symbol]['rate']
    parsed_rate = atof(rate)
    return time, parsed_rate

def get_sats_amt(amount, fiat):
   time, rate = coindesk_btc_fiat(fiat)
   btcfiat = "%.2f" % rate
   moscowtime = int(100000000/float(btcfiat))
   satstotal =  float(amount * moscowtime)
   return satstotal

@app.route('/')
def home():
    return 'SatsPay Session!'

@app.route('/about')
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


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)