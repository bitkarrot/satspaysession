from fastapi import FastAPI
from . utils import get_sats_amt

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
        content =  f"Endpoint for {fiat.upper()}, The amount is: {amount}. "
        sats = int(get_sats_amt(int(amount), fiat.upper()))
        content += f" Sats amount: {sats}"
        return content
    else:
        return f"Endpoint for {fiat}, No amount provided as integer."
