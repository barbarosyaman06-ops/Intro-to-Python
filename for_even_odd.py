less=int(input("Please Enter a Floor Number: "))
great=int(input("Please Enter a Ceiling Number: "))

even_numbers=[]
odd_numbers=[]

for x in range(less,great):
    if(x%2==0):
        even_numbers.append(x)
    else:
        odd_numbers.append(x)

print("Even Numbers: ",even_numbers,end=" ")
print("\nOdd Numbers: ",odd_numbers,end=" ")