from fastapi import FastAPI, Request

from fastapi.middleware.cors import CORSMiddleware
from tortoise import Tortoise

from postgres.config import TORTOISE_ORM
from postgres.models import MegaProjects, MegaProjectsPydantic, MegaProjectsPydanticIn


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup() -> None:
    await Tortoise.init(config=TORTOISE_ORM)
    # Generate the schema
    await Tortoise.generate_schemas(safe=True)


@app.on_event("shutdown")
async def shutdown() -> None:
    await Tortoise.close_connections()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/mega-projects")
async def get_mega_projects(request: Request):
    params = request.query_params
    return await MegaProjectsPydantic.from_queryset(MegaProjects.filter(**params))


@app.post("/mega-projects")
async def post_mega_project(mega_project: MegaProjectsPydanticIn):
    mega_project = await MegaProjects.create(**mega_project.dict(exclude_unset=True))
    return await MegaProjectsPydantic.from_tortoise_orm(mega_project)
