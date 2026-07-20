#while loop
myNumbers=[]
i=0
while(i<7):
  input_number=int(input("Please Enter a Number: "))
  myNumbers.append(input_number)
  i+=1
myNumbers.sort()

x=0
while(x<7):
  print(myNumbers[x],end=" ")
  x+=1
