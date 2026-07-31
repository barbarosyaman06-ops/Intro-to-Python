#we can use math lib to easily access square root

import math
myNumber=int(input("Please enter a number: "))
square_root=math.sqrt(myNumber)

if (square_root.is_integer()):
    print(f"Rooted number {square_root} is an integer")
else:
    print(f"Rooted number {square_root:.2f} is not an integer")