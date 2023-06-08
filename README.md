# Satspay Session

This micro app delivers a custom Invoice amount from the SatsPayExtension fron LNbits via an FastAPI endpoint. 
Why do this? Because we want to be able to specify a lightning invoice in sats with the USD amount (or any other fiat equivalent amount) with a link instead of creating it manually from within the LNBits web interface. 

URL Pattern:
https://satspaylink.vercel.app/fiat/{currency}/amt/{value}

Example: 

This is a live example, where the repo is deployed at satspaylink.vercel.app and the user specifies currency type and amount at the url: 

https://satspaylink.vercel.app/fiat/usd/amt/100 

The above link, given the parameters of 100 USD, will calculate the equivalent amount of sats and 
then redirect the user to a lightning invoice created by the satspayserver extension.

Clicking on the above link will redirect to the lnbits satspay extension with the lightning invoice conversion automatically. 

<img width="545" alt="Screenshot 2023-06-08 at 10 29 07 AM" src="https://github.com/bitkarrot/satspaysession/assets/73979971/e958e4a7-779c-443d-82cf-842ad181eb86">



## Env variables

For More information about how SatsPay Server works in LNBits, please visit the [extension page](https://github.com/lnbits/satspay)
and the [LNbits.com website](https://lnbits.com)

set your LNBits environment variables in vercel

```sh
LNBITS_WALLET='your data here'
ONCHAIN_WALLET='your data here'
LNBITS_URL='https://legend.lnbits.com'
INVOICE_API_KEY='your data here'
WEBHOOK='https://yoururlhere.com'
```

```
  headers =  {
          "Content-Type": "application/json",
          "X-Api-Key": INVOICE_API_KEY,
        }
```

Json passed in body 
```
{
  "onchainwallet": "string",
  "lnbitswallet": "string",
  "description": "string",
  "webhook": "string",
  "completelink": "string",
  "completelinktext": "string",
  "custom_css": "string",
  "time": 1,
  "amount": 1,
  "extra": "{\"mempool_endpoint\": \"https://mempool.space\", \"network\": \"Mainnet\"}"
}
```


# FastAPI + Vercel

This example shows how to use FastAPI on Vercel with Serverless Functions using the [Python Runtime](https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python).

## 1-Click Deploy to Vercel 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fbitkarrot%2Fsatspaysession&env=LNBITS_WALLET,ONCHAIN_WALLET,LNBITS_URL,WEBHOOK,INVOICE_API_KEY)


## To install

```sh
python3 -m venv venv 
source venv/bin/activate
pip install -r requirements.txt
```

## To run this app locally

```sh
uvicorn src.app:app --reload
```

Your application is now available at `http://localhost:8000`.
