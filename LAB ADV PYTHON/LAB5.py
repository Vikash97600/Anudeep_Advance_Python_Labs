# 1.Write a decorator that counts the number of times a function has been called.

from functools import wraps

def countCalls(func):
    count=0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Function {func.__name__} has been called {count} times")
        result=func(*args, **kwargs)
        return result
    return wrapper

@countCalls
def example_function():
    print("Function called")


example_function()
example_function()

# 2.Write a decorator that repeats the execution of a function a specified number of times.

def repeat(n):
    def decorator(func):
        def wrapper(*args,**kwargs):
            for i in range(n):
                result = func(*args,**kwargs)
            return result
        return wrapper
    return decorator
    

@repeat(5)
def my_data():
    print("Python programming")

my_data()