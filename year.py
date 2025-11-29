books = [
    {"id": 111, "title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
    {"id": 222, "title": "Dune", "author": "Frank Herbert", "year": 1965},
    {"id": 333, "title": "The girl with the Dragon Tattoo", "author": "Stieg Larsson", "year": 2005},
    {"id": 444, "title": "All the Light We Cannot See", "author": "Anthony Doerr", "year": 2014},
    {"id": 555, "title": "The Shining", "author": "Stephen King", "year": 1977}
]

@app.post("/books")
def add_book(book: dict):
    global counter
    new_book = {
        "id": counter, "title": book.get("title"),
        "author": book.get("author"), "year": book.get("year")
    }
    books.append(new_book)
    counter += 1
    return new_book
