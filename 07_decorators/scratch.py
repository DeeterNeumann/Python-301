def lowercase(func):
    """A decorator that avoids digital screaming."""
    def wrapper(text):
        initial_result = func(text)
        new_result = initial_result.lower()
        return new_result
    return wrapper

@lowercase
def say_something(text):
    return text

print(say_something("HEY WHAT'S UP?"))  # OUTPUT: hey what's up?

@lowercase
def echo(text):
    return text

print(f"echo {echo("ECHO")} echo")