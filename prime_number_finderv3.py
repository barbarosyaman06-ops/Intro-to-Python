#prime number list until the entered number

entered_number=int(input("Please enter a number to enlist prime numbers."))
prime_numbers=[]

if (entered_number<0):
    print("Please enter a positive number!")
elif (entered_number>0 and entered_number<2):
    print("There are no prime numbers in this interval!")
else:
    for i in range(2,entered_number):
        for k in range(2,i):
            if (i%k==0):
                break
            else:
                prime_numbers.append(i)
print(f"The list of prime numbers: {prime_numbers}")
                
                
                
            