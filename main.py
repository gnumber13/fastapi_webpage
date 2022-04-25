from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from dataclasses import dataclass

# units.py
import units as un

# functions
def start_service(url, html_file):
    @app.get(url, response_class=HTMLResponse)
    async def read_item(request: Request):
        return templates.TemplateResponse("index.html", \
                context={"request": request, "entry_list": entry_list, "entry_html": html_file})

# update html files
un.update_html()

# start main process
app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_item():
    return "fastapi is running\n"

# setup for static templates and static content
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

entry_list = un.load_yaml_data("config.yaml.py", "menu")

for entry in entry_list:
    print(entry['url'], entry['html_file'])
    start_service(entry['url'], entry['html_file'])

