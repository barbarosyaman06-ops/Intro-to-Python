adjectives=["red","big","tasty","yellow","colorful"]
fruits=["apple","cherry","pear","melon","water melon"]


for outer in adjectives:
    for inner in fruits:
        print(outer,inner)


#inside nested for loops like the one up above first the outer loops start in
#this case it is red and the inner loop continues to print red (inner list)
#red apple,red cherry,red pear,red melon... and when it is done the other outer
#list item takes the order and keeps it going. (big apple,big cherry...)

#nested lists with for loops:

students=[[123,"Barbaros"],[234,"Uras"],[653,"Eylül"]]

for item1,item2 in students:
    print(f"Student ID: {item1} Student Name: {item2}")