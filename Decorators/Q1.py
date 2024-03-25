# Write a decorator that measures the time a function takes to execute

import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__time__} ran in {end - start} time")
        return result

    return wrapper
@timer
def ex_fun(n):
    time.sleep(n)

    ex_fun(2)