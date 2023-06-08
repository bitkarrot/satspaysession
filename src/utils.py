from locale import atof, setlocale, LC_NUMERIC
import requests

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


if __name__ == '__main__':
    try:
        fiat = 'usd' # Must be upper case
        amount = 100 # Must be integer
        total = get_sats_amt(amount=amount, fiat=fiat.upper())
        print("Fiat: ", fiat, "Amount:", amount)
        print("Total: ", total)
    except Exception as e:
        print(e)