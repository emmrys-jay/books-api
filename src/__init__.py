from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager
from src.db.main import initdb


@asynccontextmanager
async def life_span(app: FastAPI):
    print("server is starting...")
    await initdb()
    yield
    print("server has been stopped")


version = "v1"

app = FastAPI(
    title="Books API",
    description="A RESTFUL API for managing book reviews",
    version=version,
    lifespan=life_span,
)

app.include_router(book_router, prefix=f"/api/{version}/books", tags=["books"])
