#prime number detector via using root operation
isPrime=True
input_number=int(input("Please enter a number to examine: "))

if (input_number<0):
  print("Please enter a positive number!")
elif (input_number>0 and input_number<2):
  print("The smallest prime number is 2 please enter a differnt number!")
else:
  for i in range(2,int(input_number**0.5)+1):
    if(input_number %i ==0):
      isPrime=False
      break
  if(isPrime):
      print(f"{input_number} is a prime number!")
  else:
      print(f"{input_number} is not a prime number!")