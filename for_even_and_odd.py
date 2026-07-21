#even or odd number generator via for and continue:

less=int(input("Please Enter a Number"))
great=int(input("Please Enter a Number"))


for item in range(less,great):
    if(item%2==0):
        print("Even Printer Output: ",item)
    else:
        print("Odd Printer Output: ",item)
    

