#Python Decorators

def outer_function(name):
    def greeting():
        return f"Hello, {name}"
    return greeting()

print(outer_function(4))


def decorator_function(func):
    def wrapper_function(*args, **kwargs):
        print(f"start")
        result=func(*args, **kwargs)
        print(f"end")
        return result
    return wrapper_function

@decorator_function
def my_message():
    print("This is an example function")

my_message()