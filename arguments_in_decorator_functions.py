#decorator functions

def flexible_decorator(func):
    def wrapper(*args,**kwargs):
        print(f"Functions Name: {func.__name__}")
        if (args):
            print(f"Args: {args}")
        if (kwargs):
            print(f"Key value args: {kwargs}")
        result=func(*args,**kwargs)
        print(f"'{func.__name__}' function's result is: {result}\n")
        return result
    return wrapper

@flexible_decorator
def add(x,y):
    return x+y

@flexible_decorator
def greet(name,age,country):
    return f"Hi {name}, your age is {age}, your country is {country}."

@flexible_decorator
def multiply_and_sum(*numbers,factor):
    return sum(numbers)*factor


add(3,4)
greet("Barbaros",age=20, country="Türkiye")
multiply_and_sum(2,5,6,7,8,3,5,7,factor=5)