#membership operators such as in is used to identify a specific value in a list or a tuple.

food=["chicken","meat","fish","mutton","rabbit"]
print("grape" in food)

dish=["chicken","meat","fish","mutton","rabbit","soup"]
print("apple" not in dish)

#& and | operators are bitwise operators and applies their same logic to bitwsie levels
x=6 & 3
print(x) #output 2

#6 is 00000110
#3 is 00000011
#we aplly the and logic which results in:
# 00000010 = 2

y=6 | 3
print(y) #output 7
#6 is 00000110
#3 is 00000011
#we muyltiply as in or logical operator
# 00000111 = 7

z=6 ^ 3
print(z) #output 5
#we write the bitwise 6 and 3 and apply xor logic to have 5.

a=3<<2
print(a) #leftshifts the bits by 2 digits. and returns a bit which results in a numeric number. multiply the number by the shifted exponent of two
#returns 12
b=32>>2
print(b) #applies the opposite logic as the previous operator. divide the number by the shifted exponent of two
#returns 8

c=~245
print(c) #output -246
#bitwise finds the 246, finds 247 finds -247. then adds 1 to 247 and elevate to -247.

#() paranthesis has the order of operations

d=5+(12**6)
print(d)



