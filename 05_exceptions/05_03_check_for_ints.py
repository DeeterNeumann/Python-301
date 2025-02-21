# Create a script that asks a user to input an integer, checks for the
# validity of the input type, and displays a message depending on whether
# the input was an integer or not.
# The script should keep prompting the user until they enter an integer.

def is_it_int(test):
    try:
        int(test)
        return True
    except ValueError:
        return False
    
user_input = ""

while type(user_input) != int:
    user_input = input("Enter an integer: ")
    if is_it_int(user_input):
        break
    else:
        print("Not an integer. Enter an integer")

print("You entered an integer!")
