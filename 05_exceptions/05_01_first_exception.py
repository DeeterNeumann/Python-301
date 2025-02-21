# Write a script that generates an exception.
# Handle this exception with a try/except block.
# For example:
#
# list_ = ["hello world!"]
# print(list_[1])
#
# This raises and exception that needs to be handled.

list_ = ["hello world!"]

try:
    print(list_[1])
except:
    # if len(list_) < 2:
    print("This list only contains a single item and should be indexed as 0 (i.e., 'list_[0]')")

#arbitrary code executions - running any code by manipulating
#