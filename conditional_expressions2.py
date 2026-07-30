#if we have 2 or more if,else statements we must use and or or in order to merge them


a=70
b=19
c=123

if(a>b and c>a):
    print("Both conditions are ture")

if(not a>b):
    print(f"{a} is not greater than {b}")

#a>b which returns true, Since not statement coberts true to false, the print code
#never runs because it cant find any True bool to run.