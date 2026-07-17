#array=series
#lists help us store multiple amount of items in a single variable.
#array means lists,tuples,dictionaries and sets.

# vegetables=["cucumber","tomato","patato","eggplant","parsley","herbs"]

# print(vegetables) 

# #lists store variables with a index number which leds two similar strings to be stored indifferently.
# fruit=["orange","orange","orange"] #despite repeated three times pyhton acknowladge them as a individual entity due to index numbers.
# print(fruit[0])
# #most recent added item will be the last element off the list.

# print(len(fruit))

#lists can hold various types of data (integers,strings,bools)
#there are different types of collection elements,and they become handy in varying situations
#lists are in-line,changeble,repetetive
#tuples are in-line,unchangeble,repetetive
#sets are not in-line,unchangble,not repetetive
#dictionaries are in-line,changeble,not repetetive 

newlist=["uras","furkan","yağız","taha"]
print(newlist[2:5])
#this method includes 2 but exclude 5 so the interval is [2,5)
 

if "uras" in newlist:
    print("Yes,this name is in the list")
else:
    print("No, this name is not in the list")

grocery_list=["toilet paper","peanut butter","milk","nutella"]
print(grocery_list)
grocery_list[2]="Orange Juice"
print(grocery_list)

#variable_name[index number]="new element" adjusts the desired element to a new element.
#also we can give an interval using [:] method
grocery_list[0:3]=["Tomato","Cucumber","Eggplant"]
print(grocery_list)