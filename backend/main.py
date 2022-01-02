from fastapi import FastAPI, Request, status

from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from tortoise import Tortoise
from tortoise.validators import ValidationError

from postgres.config import TORTOISE_ORM
from postgres.models import MegaProjects, MegaProjectsPydantic, MegaProjectsPydanticIn


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(ValidationError)
async def orm_error_handler(request: Request, exception: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": str(exception)}
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
