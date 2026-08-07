def my_name(name3,name2,name1):
    print("My real name is "+name3)

my_name(name1="Murat",name2="Şükrü",name3="Barbaros")

def new_function(**kwargs):
    print("His last name is "+kwargs["lastname"])

new_function(firstname="Barbaros",lastname="YAMAN")

def my_country(country="Türkiye"):
    print("I am from "+country)

my_country()

def my_school_function(school):
    for item in school:
        print(item)

US=["MIT","Stanford","Berkeley","Harvard"]

my_school_function(US)


def math_function(x):
    return x*7

result12=math_function(3)
print(math_function(15))
print(math_function(12))
print(math_function(89))


def sum_function(x,y):
    result=x+y
    return result

new=sum_function(12,15)

print(new) 

print(sum_function(sum_function(4,12),12))