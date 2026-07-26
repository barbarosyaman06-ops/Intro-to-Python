#prime number detector.

input_number=int(input("Please Enter a Number to examine: "))

if(input_number<0):
    print("You have entered a negative number. Please enter a positive number.")
elif(input_number>0 and input_number<2):
    print("The smallest prime number is 2. Please enter a different number.")
else:
    for i in range(2,input_number):
        if input_number % i==0:
            print(f"The entered {input_number} is not a prime number")
            break
        else:
            print(f"The entered {input_number} is a prime number!")


        
    




