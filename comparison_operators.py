# x=7
# y=19
# print(x==y)

# if x>y:
#     print(f"{x} is bigger than {y}.")
# else:
#     print(f"{x} is less than {y}.")

#we use !=  to indicate that the comparents are not equal.
#> is greater than and < is less than which are used for comparing numerics.
#>= means greater than or equal to. and the opposite signed version uses the same logic.


x=7
y=5

if x>=y:
    print(f"{x} is greater than or equal to {y}.")
else:
    print(f"{x} is less than {y}")


#password comparator
truepassword="1616"
challengingpassword=input("Enter The Password: ")

if truepassword != challengingpassword:
    print("System blocked!")
else:
    print("Congratulations!")

#Mr fehmi uyar (the instructor of the course that im following) 
#advices to use not equal comparator first and to be able to advance with elif's 
#to ease the comparison


#even or odd comparator

number=int(input("Enter a number: "))

if number<0:
    print("The entered number should be grater than zero.")
elif number%2 ==0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

#% modulus is very important to indicate odd or even numbers.