# In this exercise, you will practice both File I/O as well as using Exceptions
# in a real-world scenario.
#
# This folder contains another folder called `books/` that contains three text files
# of books from Project Gutenberg:
# 1. war_and_peace.txt
# 2. pride_and_prejudice.txt
# 3. crime_and_punishment.txt
#
# 1) Open `war_and_peace.txt`, read the whole file content and store it in a variable
# 2) Open `crime_and_punishment.txt` and overwrite the whole content with an empty string
# 3) Loop over all three files and print out only the first character each. Your program
#    should NEVER terminate with a Traceback.
#     a) Which exception can you expect to encounter? Why?
#     b) How do you catch it to avoid the program from terminating with a traceback?

war_and_peace ="05_exceptions/books/war_and_peace.txt"
pride_and_prejudice = "05_exceptions/books/pride_and_prejudice.txt"
crime_and_punishment = "05_exceptions/books/crime_and_punishment.txt"


with open(war_and_peace, "r", encoding ="utf-8") as wp_file:
     read_war_and_peace = wp_file.read()
print(read_war_and_peace)
  
with open(crime_and_punishment, "w") as cp_file:
    cp_file.write("")
# print(overwrite_crime_and_punishment)

books = [war_and_peace, pride_and_prejudice, crime_and_punishment]

for book in books:
    try:
        with open(book, "r", encoding="utf-8") as file:
            book_first_character = file.read()
        print(book_first_character[0])
    except IndexError:
        print(f"The file, {book}, did not contain any characters.")
    
        