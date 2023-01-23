from fastapi import FastAPI

from .api import profile


def create_application() -> FastAPI:
    app = FastAPI()

    # Routers
    app.include_router(profile.router, prefix="/profile")

    return app


app = create_application()
