x=15

print(x>12 or x<3)

#and demands a 1(true) to run as a product of 2 boolean data.
#or only demands 1 true to return 1(true).

exam_score=int(input("Enter your exam score: "))

if exam_score<50:
    print("You have failed the exam :(")
elif 50<=exam_score and exam_score<85:
    print("You have sucessfully passed the test!")
else:
    print("You are a top %1 student!")


#not returns the anonym of the boolean data we are expecting.

# x=6
# print(not(x>4 and x<7))

#is is used to compare the same valued list variables and byte storages. is returns false despite two different variables contataining the same items.
#is not is used to seperate two same variables

x=["mechanical","chenical","aerospace","enviorment"]
y=["mechanical","chenical","aerospace","enviorment"]
z=x

print(x is z)
print(x is y)
print(x==y)
