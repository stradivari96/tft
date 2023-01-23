import asyncio
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from .api import summoners
from .service.riot import get_user


def create_application() -> FastAPI:
    app = FastAPI()
    templates = Jinja2Templates(directory=Path(__file__).parent / "templates")

    # Routers
    app.include_router(summoners.router, prefix="/summoner")

    @app.get("/", response_class=HTMLResponse)
    async def homepage(request: Request):
        summoners = ["stradivari96", "frenfrenburger", "raconma"]
        data = await asyncio.gather(*(get_user(s) for s in summoners))
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "summoner_data": data,
            },
        )

    return app


app = create_application()
