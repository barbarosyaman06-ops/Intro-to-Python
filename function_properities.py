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
