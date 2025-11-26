from fastapi import FastAPI, HTTPException

app = FastAPI()

# "ןורכיזב "םינותנ דסמ
books = [
    {"id": 111, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"id": 222, "title": "Dune", "author": "Frank Herbert"},
    {"id": 333, "title": "The girl with the Dragon Tattoo", "author": "Stieg Larsson"},
    {"id": 444, "title": "All the Light We Cannot See", "author": "Anthony Doerr"},
    {"id": 555, "title": "The Shining", "author": "Stephen King"}
]
counter = 5

@app.get("/books")
def get_books():
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books")
def add_book(book: dict):
    global counter
    new_book = {
        "id": counter, "title": book.get("title"),
        "author": book.get("author")
    }
    books.append(new_book)
    counter += 1
    return new_book

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")