#via pip
import uvicorn

#custom
from application import fastapi_app

app = fastapi_app("static", "markdown")

app.mount_static_content()

# everything with .d ending in markdown folder
app.assemble_blogs()

app.assemble_html()

app.enable_service()

uvi_entrypoint = app.app

if __name__ == "__main__":
    uvicorn.run("main:uvi_entrypoint", port=5000, log_level="info")
