#via pip
import uvicorn

#custom
import application as applib
from application import app

#myapp = fastapi_app("static", "markdown")

applib.mount_static_content()

# everything with .d ending in markdown folder
applib.assemble_blogs()

applib.assemble_html()

applib.enable_service()

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info")
