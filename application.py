#via stdlib
import sys
import os

#via pip
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

#custom
import units as un


app = FastAPI()
app_root = os.path.dirname(__file__)


config_file = app_root + "/" + "config.yaml"

project_config = un.load_yaml_data(config_file, "project_config")

assets_path = project_config['assets_path']

md_path = project_config['md_path']



def assemble_blogs():
    un.concat_blogs(md_path, app_root)

def assemble_html():
    un.update_html(app_root, config_file)

def enable_service():
    #optional root api
    entry_list = un.load_yaml_data(config_file, "menu")

    @app.get("/test", response_class=HTMLResponse)
    async def read_item():
        return "fastapi is running\n"

    for entry in entry_list:
        html_path = "html_renders/" + entry['html_file']
        print(html_path)
        enable_url_response(entry['url'], html_path, entry_list)

def enable_url_response(url, html_file, entry_list):
    templates = Jinja2Templates(directory=app_root + "/templates")
    @app.get(url, response_class=HTMLResponse)
    async def read_item(request: Request):
        return templates.TemplateResponse("index.html", \
                context={"request": request, "entry_list": entry_list, "entry_html": html_file })

def mount_static_content():
    # setup for static templates and static content
    print("assets =>>>" + assets_path)
    mnt_path="/static"
    app.mount(mnt_path, StaticFiles(directory=assets_path), name=assets_path)

