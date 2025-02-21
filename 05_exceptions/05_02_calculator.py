# Write a script that takes in two numbers from the user and calculates the quotient.
# Use a try/except statement so that your script can handle:
#
# - if the user enters a string instead of a number
# - if the user enters a zero as the divisor
#
# Test it and make sure it does not crash when you enter incorrect values.



try:
    numerator = int(input("Enter the number to be divided: "))
    denominator = int(input("Enter a number to divide your first number by: "))
    
    quotient = numerator/denominator
    print("Quotient:", quotient)

except ValueError:
    print("The last number you entered is not a digit. Enter the numbers as digits (e.g., 5, 22, 37)")

except ZeroDivisionError:
    print("You cannot divide by 0!")