# Create a custom decorator function that records the execution time of
# the decorated function and prints the time to your console when the function
# has finished execution.

import time
import datetime

def function_time(initial_func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = initial_func(*args, **kwargs)
        time_delta = time.time() - start_time
        print(f"It took {time_delta} seconds to run {initial_func.__name__}")
        return result
    return wrapper

@function_time
def do_something():
    time.sleep(2)

@function_time
def sleep_time(sleep_time):
    time.sleep(sleep_time)

do_something()

sleep_time(2)

def time_it(initial_func):
    def wrapper_func():
        time = datetime.datetime.now()
        result = f"{initial_func()} {time}"
        print(result)
        return result
    return wrapper_func

@time_it
def code_execution():
    return "Code Executed at:"

@time_it
def current_time():
    return "The current time is:"

code_execution()
current_time()