def output():
    print("This is a function that outputs a message.")

output()

def my_name(fname):
    print(fname +" Yaman")

my_name("Barbaros")

def fullname(firstname,lastname):
    print(firstname+" "+lastname)

fullname("Barbaros","Yaman")

def new_function(*args):
    print("My real name is "+args[2])

new_function("Barbaros","Yaman","Yiğit","Serap")