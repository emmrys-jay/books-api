from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Clean Code: A Handbook of Agile Software Craftsmanship",
        "author": "Robert C. Martin",
        "publisher": "Prentice Hall",
        "published_date": "2008-08-01",
        "page_count": 464,
        "language": "English",
    },
    {
        "id": 2,
        "title": "The Pragmatic Programmer: Your Journey to Mastery",
        "author": "Andrew Hunt and David Thomas",
        "publisher": "Addison-Wesley Professional",
        "published_date": "1999-10-20",
        "page_count": 352,
        "language": "English",
    },
    {
        "id": 3,
        "title": "You Don’t Know JS Yet: Scope & Closures",
        "author": "Kyle Simpson",
        "publisher": "O'Reilly Media",
        "published_date": "2020-01-28",
        "page_count": 143,
        "language": "English",
    },
    {
        "id": 4,
        "title": "Introduction to the Theory of Computation",
        "author": "Michael Sipser",
        "publisher": "Cengage Learning",
        "published_date": "2012-01-27",
        "page_count": 504,
        "language": "English",
    },
    {
        "id": 5,
        "title": "Design Patterns: Elements of Reusable Object-Oriented Software",
        "author": "Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides",
        "publisher": "Addison-Wesley Professional",
        "published_date": "1994-10-31",
        "page_count": 395,
        "language": "English",
    },
]


class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str


class BookUpdate(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str


@app.get("/books", response_model=List[Book])
async def get_books():
    return books


@app.post("/books", status_code=status.HTTP_201_CREATED)
async def create_book(book: Book) -> dict:
    new_book = book.model_dump()

    books.append(new_book)

    return new_book


@app.get(
    "/books/{book_id}",
)
async def get_book(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Book was not found"
    )


@app.patch("/books/{book_id}")
async def update_book(book_id: int, body: BookUpdate) -> dict:
    for book in books:
        if book["id"] == book_id:
            book["title"] = body.title
            book["publisher"] = body.publisher
            book["author"] = body.author
            book["language"] = body.language
            book["page_count"] = body.page_count

            return book

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Book was not found"
    )


@app.delete("/books/{book_id}")
async def delete_book(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            books.remove(book)

            return {"detail": f"successfully deleted book with id {book_id}"}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Book was not found"
    )
