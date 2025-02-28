# Write a decorator function that wraps text output into quotes, e.g.:
# Hello world! ----> "Hello World!"
# You can use it to create quotes from text output.

def quoter(initial_func):
    def wrapper(*args, **kwargs):
        quoted = f'"{initial_func(*args, **kwargs)}"'
        print(quoted)
        return quoted
    return wrapper

@quoter
def say_something(something):
    return something

say_something("well hello there")
say_something(3)