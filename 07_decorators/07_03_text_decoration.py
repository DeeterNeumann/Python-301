# Write a decorator that literally decorates text output.
# Make it so the symbol it uses can be an argument to the decorator
#
# The output of a function that returns `"Hello"` that has been
# decorated like with `@decorate("*")` should look like this:
#
# ******************************
# Hello
# ******************************

# 30 asteriks

def make_fancy(symbol):
    def decorator_func(initial_func):
        def wrapper(*args, **kwargs):
            fancy = f"{symbol * 30}\n{initial_func(*args, **kwargs)}\n{symbol * 30}"
            print(fancy)
            return fancy
        return wrapper
    return decorator_func

@make_fancy("*")
def to_be_decorated(word):
    return word

@make_fancy("#")
def decorate_again(word):
    return word

to_be_decorated("hello")

decorate_again("goodbye")