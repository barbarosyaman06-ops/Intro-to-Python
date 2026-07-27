#enhanced version from tutor

entered_number=int(input("Please enter a number: "))
prime_numbers=[]

if (entered_number<0):
    print("Please enter a positive number!")
elif (entered_number>=0 and entered_number<2):
    print("The smallest prime number is 2!")
else:
    prime_numbers.append(2)
    for i in range(3,entered_number+1,2):
        for k in range(3,int(i**0.5)+1):
            if (i%k==0):
                break
        else:
            prime_numbers.append(i)
    print(f"{prime_numbers}")