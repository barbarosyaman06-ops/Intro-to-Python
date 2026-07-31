#conditional expressions - is rooted number an integer or not?

entered_number=int(input("Please enter a number to root: "))

root=entered_number**0.5

if root == int(root):
    print(f"{int(root)}")
else:
    print(f"The rooted number you entered is not an integer")
    print(f"{root}")

