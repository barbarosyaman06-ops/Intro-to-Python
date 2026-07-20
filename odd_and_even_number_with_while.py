#odd and even numbers displayed within a selected interval by operator

floor_integer=int(input("Please Enter a Floor Number: "))
ceiling_integer=int(input("Please Enter a Ceiling Number: "))

myEvenNumbers=[]
myOddNumbers=[]

while(floor_integer<=ceiling_integer):
  if(floor_integer%2 ==0):
    myEvenNumbers.append(floor_integer)
  else:
    myOddNumbers.append(floor_integer)
  floor_integer+=1

print("\nEven Numbers: ",myEvenNumbers)
print("\nOdd Numbers: ",myOddNumbers)


