from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field


app = FastAPI(title="Books API")


class BookIn(BaseModel):
    title: str
    author: str
    year: int = Field(gt=0)


class Book(BookIn):
    id: int


books: list[Book] = []
next_id = 1


@app.get("/books")
def get_books() -> list[Book]:
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int) -> Book:
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(payload: BookIn) -> Book:
    global next_id
    book = Book(id=next_id, **payload.model_dump())
    books.append(book)
    next_id += 1
    return book


@app.put("/books/{book_id}")
def update_book(book_id: int, payload: BookIn) -> Book:
    for index, existing in enumerate(books):
        if existing.id == book_id:
            updated = Book(id=existing.id, **payload.model_dump())
            books[index] = updated
            return updated
    raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{book_id}")
def delete_book(book_id: int) -> dict[str, str]:
    for index, book in enumerate(books):
        if book.id == book_id:
            books.pop(index)
            return {"message": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")