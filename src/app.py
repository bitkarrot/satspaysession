from fastapi import FastAPI, Request, Body, Header
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import starlette.status as status
from typing import Optional
import http
import logging

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

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name='static')
templates = Jinja2Templates(directory='templates/')



def handle_params(fiat, amount, description):
    if type(amount) is int:
        sats = int(get_sats_amt(int(amount), fiat.upper()))
        res_url = get_lnbits_satspay(sats, description=description)
        print("handlparams response: ", res_url)
        return res_url
    else: 
        return f"Endpoint for {fiat}, No amount provided as integer."
    

@app.get('/fiat/{fiat}/amt/{amount}')
async def dynamic_endpoint(fiat: str, amount: int):
    res_url = handle_params(fiat, amount, '')
    if is_https_url(res_url): 
        return RedirectResponse(url=res_url, status_code=302)
    else: 
        return res_url


@app.get('/fiat/{fiat}/amt/{amount}/desc/{description}')
async def dynamic_longendpoint(fiat: str, amount: int, description: str):
    res_url = handle_params(fiat, amount, description)
    if is_https_url(res_url): 
        return RedirectResponse(url=res_url, status_code=302)
    else: 
        return res_url


@app.get("/")
async def initial_page(request: Request):
  fiat = "USD"
  description = "Meeting"
  return templates.TemplateResponse("index.html",
                                      context={
                                          'request': request,
                                          'title': "SatsPay Link",
                                          'fiat': fiat,
                                          'description': description,
                                          'amount': 100,
                                      })

@app.get("/thanks")
async def thanks_page(request: Request):
    return templates.TemplateResponse("thanks.html", context={'request': request})    


@app.post("/thanks", status_code=http.HTTPStatus.ACCEPTED)
async def thanks_post(request: Request, x_hub_signature: str = Header(None)):
     # Process the captured data as needed
    payload= await request.body()
    print("thanks data:", str(payload))  # TODO: Optionally forward tx webhook data to smtp ext.
    return templates.TemplateResponse("thanks.html", context={'request': request})    


@app.get('/about')
def about():
    return 'About'

