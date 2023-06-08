from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from . utils import get_sats_amt, get_lnbits_satspay, is_https_url

title = "satspay session"
description = "simple url bridge to lnbits satspay extension"

app = FastAPI(
    title=title,
    description=description,
    version="0.0.1 alpha",
    contact={
        "name": "bitkarrot",
        "url": "http://github.com/bitkarrot",
    },
    license_info={
        "name": "MIT License",
        "url": "https://mit-license.org/",
    },
)

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



@app.get('/fiat/{fiat}/amt/{amount}')
def dynamic_endpoint(fiat: str, amount: int):
    if type(amount) is int:
        sats = int(get_sats_amt(int(amount), fiat.upper()))
        content =  f"Endpoint for {fiat.upper()}, The amount is: {amount}. "
        content += f" Sats amount: {sats}"
        print(content)

        res_url = get_lnbits_satspay(sats)
        print("\n\n Repsonse URL: ", res_url)
        
        if is_https_url(res_url): 
            # Redirect to an external URL
            return RedirectResponse(url=res_url, status_code=302)
        else: 
            return res_url
    else:
        return f"Endpoint for {fiat}, No amount provided as integer."
