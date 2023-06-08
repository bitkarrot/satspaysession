from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import starlette.status as status
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


# initial get for index page
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

# @app.post("/link")
# async def link_page(request: Request, fiat: str = Form(None), amount: int = Form(None), description: str = Form(None)):
#     try:
#         # validation check
#         if fiat is None:
#             return RedirectResponse('/', status_code=status.HTTP_302_FOUND)
#         if amount is None:
#              return RedirectResponse('/', status_code=status.HTTP_302_FOUND)

#         url = str(request.url).split("/")
#         base_url =  "/".join(url[:-1])
#         satslink = base_url

#         if description is None:
#             satslink += f"/fiat/{fiat}/amt/{amount}"

#         if description is not None:
#             desc = "-".join(description.split())
#             satslink +=  f"/fiat/{fiat}/amt/{amount}/desc/{desc}"

#         return templates.TemplateResponse("index.html",
#                                     context={
#                                         'request': request,
#                                         'title': "SatsPay Link",
#                                         'fiat': fiat,
#                                         'description': description,
#                                         'amount': 100,
#                                         'satslink': satslink
#                                     })
#     except Exception as e:
#             logging.error(e)


@app.get('/about')
def about():
    return 'About'

