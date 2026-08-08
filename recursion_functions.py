def multiply(number):
  return number*7

def sum(x,y):
  return x+y

def my_function(func_name,my_value1,myvalue2):
  return func_name(my_value1,myvalue2)

result=my_function(sum,10,11)
print(result)

x="Awesome"
def print_function():
  x="fantastic"
  print(f"Python is {x}")

print_function()
print(f"Pyhton is {x}")

y="good"

def new_function():
    global y
    y="fantastic"
    print(f"Pyhton is {y}")

new_function()
print(y)


#recursion

def fac(n):
  if (n==0 or n==1):
    return 1
  else:
    return n * fac(n-1)


print(fac(5))

def fibonacci(n):
  if (n==0):
    return 0
  elif n==1:
    return 1
  else:
    result=fibonacci(n-1) + fibonacci(n-2)
    return result

for item in range(6):
  print(fibonacci(item),end=" ")




