from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import sys
import os

import units as un


class fastapi_app():
    # create new FastAPI() object
    app = FastAPI()

    app_root = os.path.abspath(os.curdir)

    def __init__(self, static_assets, md_path):
        self.assets_path = self.app_root + "/" + static_assets
        self.md_path = self.app_root + "/" + md_path

    def assemble_blogs(self):
        un.concat_blogs(self.md_path)

    def assemble_html(self):
        un.update_html()

    def enable_service(self):
        #optional root api
        entry_list = un.load_yaml_data("config.yaml.py", "menu")

        @self.app.get("/", response_class=HTMLResponse)
        async def read_item():
            return "fastapi is running\n"

        for entry in entry_list:
            html_path = "html_renders/" + entry['html_file']
            print(html_path)
            self.enable_url_response(entry['url'], html_path, entry_list)

    def enable_url_response(self, url, html_file, entry_list):
        templates = Jinja2Templates(directory="templates")
        @self.app.get(url, response_class=HTMLResponse)
        async def read_item(request: Request):
            return templates.TemplateResponse("index.html", \
                    context={"request": request, "entry_list": entry_list, "entry_html": html_file })

    def mount_static_content(self):
        # setup for static templates and static content
        print("assets =>>>" + self.assets_path)
        mnt_path="/static"
        self.app.mount(mnt_path, StaticFiles(directory=self.assets_path), name=self.assets_path)

