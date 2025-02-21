# Read in the first number from `integers.txt`
# and perform a calculation with it.
# Make sure to catch at least two possible Exceptions (`IOError` and `ValueError`)
# with specific `except` statements, and continue to do the calculation
# only if neither of them applies.

file_name = 'integers.txt'


try:
    with open(file_name, "r") as file:
        content = file.read()
        int_list = content.split()
    calculation = int(int_list[0]) - 27
except IOError as e:
    print(f"IOError occurred: {e}")
except ValueError:
    print("You can only do this calculation with an integer.")
else:
    print(calculation)




