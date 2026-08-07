def myfunction():
  pass

def new_function(x,/):
   print(x)

new_function(7)

def latest_function(*,y):
   print(y)

latest_function(y=9)

def different_function(k):
   print(k)

different_function(k=19)


def seperator(a,b,/,*,c,d):
   print(a+b+c+d)

seperator(7,8,c=14,d=19)


def control(number):
   if (number>0):
      result="Positive"
   elif (number==0):
      result="Neutral"
   else:
      result="Negative"
   return result

print(control(5))
print(control(-16))
print(control(0))


def square(number):
   result=number**2
   return result

def sum_and_square(x,y):
   calculation=x+y
   return square(calculation)

result=sum_and_square(3,4)
print(result)


def outer_function(name):
   def greeting():
      return f"Hello, {name}!"
   return greeting()

print(outer_function("Barbaros"))


def sum(x,y):
   return x+y

def multiply(x,y):
   return x*y

def calculation(x,y):
   sum_result=sum(x,y)
   multiply_result=multiply(x,y)
   return sum_result,multiply_result


result=calculation(12,5)
print(result)