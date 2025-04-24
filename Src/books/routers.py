from fastapi import APIRouter, HTTPException, status, Path
from typing import List
from Src.books.book_data import books
from Src.books.schemas import Book, UpdateBook


book_router = APIRouter()


@book_router.get("/", response_model=List[Book])
async def get_all_books():
    return books

@book_router.post("/",status_code=status.HTTP_201_CREATED, response_model=Book, summary="Create a new book")
async def create_book(book:Book) -> dict:
    new_book = book.model_dump()
    books.append(new_book)
    return new_book

@book_router.get("/{id}")
async def get_book(id: int = Path(...,description="ID of book")) ->dict:
    for book in books:
        if book["id"] == id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@book_router.patch("/{id}")
async def update_book(id: int, book_update:UpdateBook) -> dict:
    for book in books:
        if book["id"] == id:
            book["title"] = book_update.title if book_update.title else book["title"]
            book["publisher"] = book_update.publisher if book_update.publisher else book["publisher"]
            book["page_count"] = book_update.page_count if book_update.page_count else book["page_count"]
            book["language"] = book_update.language if book_update.language else book["language"]
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@book_router.delete("/{id}")
async def delete_book(id: int) -> dict:
    for book in books:
        if book["id"] == id:
            books.remove(book)
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")