import datetime

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

def outer_func():
    msg = "Weeeeeekend!"
    def inner_func():
        print(msg)
    return inner_func

# outer_func() #OUTPUT: NOTHING!

say_wee = outer_func()

say_wee()


def outer_func(msg):
    def inner_func():
        print(msg)
    return inner_func

say_wee = outer_func("weee")
say_wee()

say_no = outer_func("noooo")
say_no()

# def decorator_func(initial_func):
#     def wrapper_func():
#         return initial_func()
#     return wrapper_func

# def prettify():
#     print("flowers")

# decorated_prettify = decorator_func(prettify)

# decorated_prettify()

# def dogify():
#     print("WOOF")

# decorated_dogify = decorator_func(dogify)

# decorated_dogify()

def decorator_func(initial_func):
    def wrapper_func():
        print("the wrapper function picked some...")
        return initial_func()
    return wrapper_func

@decorator_func
def prettify():
    print("flowers for you")

# decorated_pretty = decorator_func(prettify)

# decorated_pretty()

# prettify = decorator_func(prettify)
prettify()


def repeat_decorator(initial_func):
    def wrapper_func():
        print(f"{initial_func()}")
        print(f"{initial_func()}")
        return initial_func()
    return wrapper_func

@repeat_decorator
def pizza():
    return "pizza"

@repeat_decorator
def hoagies_and_grinders():
    return "hoagies and grinders"

pizza()

hoagies_and_grinders()

# time = datetime.datetime.now()

def time_it(initial_func):
    def wrapper_func():
        time = datetime.datetime.now()
        result = initial_func()
        print(time)
        return result
    return wrapper_func

@time_it
def code_execution():
    print("Code Executed at:")

@time_it
def current_time():
    print("The current time is: ")

code_execution()
current_time()

def add_message_from(name):
    def decorator_func(initial_func):
        def wrapper_func(*args):
            print(f"{name} picked some")
            return initial_func(*args)
        return wrapper_func
    return decorator_func

@add_message_from("Zeek")
def prettify(msg):
    print(msg)

prettify("flowers for you")

@add_message_from("Zeek")
def prettyify(msg):
    print(msg)

prettify("...whoops nevermind")

def say_hi():
 print("Hi.")
def say_moo():
 print("moooooooo!")
function_list = [say_hi, say_moo()]
print(function_list)
