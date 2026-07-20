#Name printer with error sensing
while True:
  name=input("Please Enter Your Name")
  if name.isidentifier():
    break
  else:
    print("Error: Please enter a valid name! ")



