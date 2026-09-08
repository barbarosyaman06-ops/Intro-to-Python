#decorator example and methods

def decorator_function(func):
    def wrapper_function(*args,**kwargs):
        print(f"The {func.__name__} is being called")
        result=func(*args,**kwargs)
        print(f"The {func.__name__} call has finished")   
        return result
    return wrapper_function





@decorator_function
def my_message():
    print("Hello Barbaros Ymaman!")
@decorator_function
def my_message1():
    print("Hello Barbaros Ymaman!")
@decorator_function
def my_message2():
    print("Hello Barbaros Ymaman!")
@decorator_function
def my_message3():
    print("Hello Barbaros Ymaman!")





my_message()
my_message1()
my_message2()
my_message3()