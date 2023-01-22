from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


def create_application() -> FastAPI:
    app = FastAPI()
    templates = Jinja2Templates(directory=Path(__file__).parent / "templates")

    # Routers
    # app.include_router(search.router, prefix="/search")

    @app.get("/", response_class=HTMLResponse)
    async def homepage(request: Request):
        return templates.TemplateResponse("index.html", {"request": request, "id": id})

    return app


app = create_application()
