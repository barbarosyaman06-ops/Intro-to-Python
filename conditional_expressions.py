#code follows a opeartor guided path so it is dependeant on user,
#we use code blocks and conditions to guide the flow of the code roadmap.

#I broadly know if,elif and else conditions
#so i wont rewrite unnecessary code blocks

#but like list comperhansion shortage we can also use conditional experssions
#in one row

a=int(input("Please enter a integer: "))
b=int(input("Please enter a second integer: "))

# print(f"{a} is bigger than {b}") if (a>b) else print(f"{a} is less than {b}")

#this method is called ternary opeators

#lets make a if else queue
#it is similar to nested loops actually
#the method below is short if hand

print(f"{a} is bigger than {b}") if(a>b) else print(f"{a} is equal to {b}") if(a==b) else print(f"{a} is less than {b}")


#we can't use short if hand if there is more than one code block below a if statemnet



 