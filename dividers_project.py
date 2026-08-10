def dividers(number):
  if number<0:
    print("Please try again!")
  else:
    divider_list=[]
    for starters in range(1,number+1):
      for enders in range(1,number+1):
        if starters*enders==number:
          divider_list.append(starters)
          divider_list.sort()

  print(f"The lis of all the dividers of {number} is {divider_list}")



entered_number=int(input("Please enter a number: "))
dividers(entered_number)
  
      

        


  