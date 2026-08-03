# fruits1=("apple", "banana", "cherry")
# fruits2=("kiwi", "mango", "pineapple", "papaya", "watermelon", "grapes")
# (x,y,*z)=fruits2

# print(x)
# print(y)
# print(z)

fruits=("apple", "banana", "cherry", "kiwi", "mango", "pineapple", "papaya", "watermelon", "grapes")

i=len(fruits)-1
for items in fruits:
    if (i>0):
        print(items,end="-")
    else:
        print(items)
    i=i-1


k=0
while k<len(fruits):
    if len(fruits)-1>k:
        print(fruits[k],end="-")
    else:
        print(fruits[k])
    k=k+1



 
 
 