factor=int(input("Please Enter a Number to factorize: "))

result=1
i=1
while(i<=factor):
  result*=i
  i+=1
print(f"{factor}!={result}")
