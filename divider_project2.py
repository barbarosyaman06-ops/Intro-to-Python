# def divider(number):
#     divider_list=[]
#     for item in range(1,number+1):
#         if number%item==0:
#             divider_list.append(item)

#     return divider_list



# entered_number=int(input("Please enter a number: "))

# print(divider(entered_number))

def divider(number):
    divider_list=[item for item in range(1,number+1) if number%item==0]

    return divider_list

entered_number=int(input("Please enter a number: "))
print(divider(entered_number))





