from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.routers.routes import routers
from app.core.config import configs
from app.core.container import Container
from app.utils.class_object import singleton


@singleton
class App:
    def __init__(self):
        # set app default
        self.app = FastAPI(
            title=configs.PROJECT_NAME,
            openapi_url=f"{configs.API}/openapi.json",
            version="0.0.1",
        )

        self.container = Container()

        # set cors
        if configs.BACKEND_CORS_ORIGINS:
            self.app.add_middleware(
                CORSMiddleware,
                allow_origins=[str(origin) for origin in configs.BACKEND_CORS_ORIGINS],
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"],
            )

        # set routes
        @self.app.get("/")
        def root():
            return "Service is working"

        self.app.include_router(routers)


app_creator = App()
app = app_creator.app
container = app_creator.container
