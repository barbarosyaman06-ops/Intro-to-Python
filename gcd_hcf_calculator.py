#calculating gcd:

number1=int(input("Please enter the first number: "))
number2=int(input("Please enter a second number: "))
smaller=min(number1,number2)

gcd= 1


for i in range(smaller, 0, -1):
    if (number1%i == 0 and number2%i == 0):
        gcd=i
        break

print(f"The GCD of both numbers are {gcd}")
        

lcm=(number1*number2)//gcd
print(f"The GCD of {number1} and {number2} is {lcm}")


 