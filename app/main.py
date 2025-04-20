from fastapi import FastAPI
from .database import Base, engine
from .routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Simple Task API",
    description="Une petite API pour marquer une tâche comme faite",
    version="1.0.0"
)

app.include_router(router)
