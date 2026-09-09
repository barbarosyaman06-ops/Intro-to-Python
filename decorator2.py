#Python decoraqtor function

def authentication(func):
    def wrapper(user, *args, **kwargs):
        if not user.get("auth",False):
            print("Authorization failed!")
            return
        return func(user, *args, **kwargs)
    return wrapper

@authentication
def view_account(user):
    print(f"Welcome, {user['name']}")

user1={"name":"Barbaros Yaman", "auth":True}
user2={"name": "Yiğit Yaman", "auth":False}

view_account(user1)
view_account(user2)


import time
def timer_decorator(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        result=func(*args,**kwargs)
        end_time=time.time()
        print(f"Function {func.__name__} completed in {end_time-start_time:.6f} second \n")
        return result
    return wrapper

















@timer_decorator
def slow_function(n):
    total=sum(range(n))
    print(f"Total:{total}")

@timer_decorator
def fast_function(n):
    total=sum(range(n))
    print(f"Total:{total}")

@timer_decorator
def faster_function():
    print("Faster function is completed...")


slow_function(100000000)
fast_function(1000)
faster_function()