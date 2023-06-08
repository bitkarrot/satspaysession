from locale import atof, setlocale, LC_NUMERIC
import requests
import os
import json 

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
   print("Time: ", time, "Rate: ", rate)
   btcfiat = "%.2f" % rate
   moscowtime = int(100000000/float(btcfiat))
   satstotal =  float(amount * moscowtime)
   return satstotal


INVOICE_API_KEY = os.environ['INVOICE_API_KEY']
LNBITS_WALLET = os.environ['LNBITS_WALLET']
ONCHAIN_WALLET = os.environ['ONCHAIN_WALLET']
LNBITS_URL = os.environ['LNBITS_URL']
webhook = os.environ['WEBHOOK']
sats_url = '/satspay/api/v1/charge'

def get_lnbits_satspay(sats_amount: int):
    url = LNBITS_URL + sats_url

    body = {
        "onchainwallet": ONCHAIN_WALLET,
        "lnbitswallet": LNBITS_WALLET,
        "description": "SatsPay Session",
        "webhook": webhook,
        "completelink": "",
        "completelinktext": "",
        "custom_css": "",
        "time": 1440,
        "amount": sats_amount,
        "extra": "{\"mempool_endpoint\": \"https://mempool.space\", \"network\": \"Mainnet\"}"
    }

    headers = {
            "Content-Type": "application/json",
            "X-Api-Key": INVOICE_API_KEY,
    }

    print(body)
    print(headers)
    print(url)

    try:
        # Convert the body data to JSON format
        json_data = json.dumps(body)
        response = requests.post(url, data=json_data, headers=headers)

        # Check the response status code
        if response.status_code == 200:
            # Request was successful
            res_data = response.json()
            print('Request was successful')
            print(res_data)
            charge_id = res_data['id']
            response_url = LNBITS_URL + "/satspay/" + charge_id
            return response_url

        else:
            # Request failed
            resp_data = ('Request failed with status code:', response.status_code)
            resp_data += response.text
            print(resp_data)
            return resp_data
    except Exception as e:
        print(e)
        return str(e)

def is_https_url(url):
    if url.startswith("https://"):
        return True
    else:
        return False



if __name__ == '__main__':
    try:
        fiat = 'usd' # Must be upper case
        amount = 100 # Must be integer
        total = get_sats_amt(amount=amount, fiat=fiat.upper())
        print("Fiat: ", fiat, "Amount:", amount)
        print("Total: ", total)
        res_url = get_lnbits_satspay(total)
        if is_https_url(res_url): 
            print("\n\n Repsonse URL: ", res_url)
        else: 
            print("Error messsages: " + res_url)
    except Exception as e:
        print(e)