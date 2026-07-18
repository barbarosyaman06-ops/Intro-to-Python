#we can use .sort() command to sort numbers from less to great and letters a to z.

MyNumbers=[1,24,56,43,87,95,82,71,45,12]
fruit=["Pineapple","Apple","Pear","Pomegranate"]

fruit.sort(key=str.lower)
#MyNumbers.sort()
#MyNumbers.sort(reverse=True)

# print(fruit)
# print(MyNumbers)

#we use key=str.lower paramter to ignore default mode that pritiorizes capital lettered words.
#we use reverse parameter to reverse the order set by default.
#if we want to sort numbers to a specific parameter we should define a function
#say we want to sort our number list based on a paramater of number 50
#we should substract the number from 50 and find its abouloute value to find the distance from 50 to sort them
#we can use multiple paramters via coma. exp specified sorter and reversed

def MySort(x):
  return abs(x-50)

MyNumbers.sort(key=MySort,reverse=True)

print(MyNumbers)






