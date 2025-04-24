from fastapi import FastAPI
from Src.books.routers import book_router
from contextlib import asynccontextmanager
from Src.db.main import init_db

@asynccontextmanager
async def life_span(app: FastAPI):
    print("Starting app")
    await init_db()
    yield
    print("Server Stopped")

version = "v1"
app = FastAPI(
    title = "Bookly API",
    description = "A simple API for books",
    version = version,
    lifespan=life_span
)

app.include_router(book_router, prefix=f"/api/{version}/books",tags=["books"])