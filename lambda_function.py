#lambda functions

result=lambda x: x+10

print(result(8))



names="pineapple","apple","fig","pear"

result=filter(lambda x: len(x)<4, names)

print(list(result))