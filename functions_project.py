def converter(number_string):
  if not number_string.isdigit() or len(number_string)!=4:
    print("You have entered a wrong number! Please try again")
    return
  singles= {"0": "","1": "one", "2": "two", "3":"three","4":"four","5":"five","6":"six", "7":"seven", "8":"eight", "9":"nine",}
  teens={"10":"ten", "11":"eleven", "12":"twelve", "13":"thirteen", "14":"fourteen", "15":"fifteen", "16":"sixteen", "17":"seventeen", "18":"eighteen", "19":"nineteen"}
  tens={"0":"", "2":"twenty", "3":"thirty", "4":"fourty", "5":"fifty", "6":"sixty", "7":"seventy", "8":"eight", "9":"ninety"}
  thousand_place=singles[number_string[0]]+"thousand"
  if number_string[1]!="0":
    hundred_place=singles[number_string[1]]+"hundred"
  else:
    hundred_place= ""
  tens_place=""
  ones_place=""
  if number_string[2]=="1":
    tens_place=teens[number_string[2]+number_string[3]]
  else:
    tens_place=tens[number_string[2]]
    ones_place=singles[number_string[3]]
  final=f"{thousand_place} {hundred_place} {tens_place} {ones_place}"
  output=" ".join(final.split())
  print(output)


user_input = input("Please enter a 4-digit number: ")
converter(user_input)





