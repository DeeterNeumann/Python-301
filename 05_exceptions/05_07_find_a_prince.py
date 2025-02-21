# Write a custom exception  that inherits from `Exception()`
# Open and read in the content of the book `.txt` files in the `books/` folder
# like you did in the previous exercise.
# Raise your `PrinceException()` if the first 100 characters of a book
# contain the string "Prince".

class PrinceException(Exception):
    pass
    # print(f"The prince was found (in the first 100 hundred characters) in the book!")
    
war_and_peace ="05_exceptions/books/war_and_peace.txt"
pride_and_prejudice = "05_exceptions/books/pride_and_prejudice.txt"
crime_and_punishment = "05_exceptions/books/crime_and_punishment copy.txt"

books = [war_and_peace, pride_and_prejudice, crime_and_punishment]

search_string = "prince"

# print("were starting")

for book in books:
    try:
        with open(book, "r", encoding="utf-8") as file:
            book_read = file.read()
        if search_string not in book_read[0:99].lower():
            print(f"The {search_string} was not found in the first 100 characters of {book}!")
        else:
            raise PrinceException()
    except PrinceException:
        print(f"The prince was found (in the first 100 hundred characters) in the book {book}!")