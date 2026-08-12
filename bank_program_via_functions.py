def create_account(owner_name):
  return {"owner":owner_name,"balance":0}

def deposit(account,amount):
  if amount>0:
    account["balance"]+=amount
    print(f"{amount} TL has been successfully deposited to your account. Current balance is {account["balance"] TL}")
  else:
    print("The value to be deposited must be positive")

def withdraw(account,amount):
  if amount>0:
      if account["balance"]>=amount:
          account["balance"]-=amount
          print(f"{amount} TL has been sucessfully withdrawn from your account. Current balance is {amount["balance"]}")
      else:
        print("Inadequete balance"),

def show(account):
  print(f"{account["owner"]} current balance is : {account["balance"]}")






print("Welcome to digital bank process application.")
owner=input("Account owners name: ")
account=create_account(owner)
while True:
  print("\nFunctions:")
  print("1. Deposit")
  print("2. Withdrawal")
  print("3. Show credit state")
  print("4. Exit")
  choice=int(input("Please choose a function (1-4): "))
  if(choice==1):
    amount=float(input("Enter a deposit value"))
    deposit(account,owner)
  elif(choice==2):
    amount=float(input("Please enter a value to withdraw"))
    withdraw(account,owner)
  elif(choice==3):
    show(account)
  elif(choice==4):
    print("You have exited the application successfuly. Have a nice day!")
    break
  else:
    print("You have entered an unknown number please try again!")


