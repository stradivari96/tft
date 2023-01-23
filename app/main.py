import asyncio
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from .api import profile
from .service.riot import get_profile


def create_application() -> FastAPI:
    app = FastAPI()
    templates = Jinja2Templates(directory=Path(__file__).parent / "templates")

    # Routers
    app.include_router(profile.router, prefix="/profile")

    @app.get("/", response_class=HTMLResponse, include_in_schema=False)
    async def homepage(request: Request):
        summoners = ["stradivari96", "frenfrenburger", "raconma"]
        data = await asyncio.gather(*(get_profile(s) for s in summoners))
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "summoner_data": data},
        )

    return app


app = create_application()
