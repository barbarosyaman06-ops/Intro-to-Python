#nested conditions

x=int(input("Enter an integer: "))

if(x>0):
    print("This is a positive number")
    if(x>20):
        print("This number is bigger than 20!")
    else:
        print("This number is less than 20!")
elif(x==0):
    print("This number is zero")
else:
    print("This number is a negative number")