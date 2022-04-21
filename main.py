from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from dataclasses import dataclass
import yaml
import units




filename = "notes.txt"



with open('config.yaml.py', 'r') as file:
    my_data = yaml.safe_load(file)

entry_list = my_data['menu']

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_item():
    return "fastapi is running\n"


@app.get("/home", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", \
            context={"request": request, "entry_list": entry_list, "entry_html": "home.html"})

@app.get("/news", response_class=HTMLResponse)
def read_item(request: Request):
    return templates.TemplateResponse("index.html", \
            context={"request": request, "entry_list": entry_list, "entry_html": "news.html"})

@app.get("/contact", response_class=HTMLResponse)
def read_item(request: Request):
    return templates.TemplateResponse("index.html", \
            context={"request": request, "entry_list": entry_list, "entry_html": "contact.html"})

