fruit=["watermelon","pomegrante","apple","pear","cherry"]
new_fruit=fruit+["fruit1","fruit2"]

print(new_fruit[5:])
print(len(new_fruit))

#we can use "+" to add items to lists

vegetable1=["cucumber","tomato","eggplant"]
vegetable2=["parsley","garlic","carrot","cabbage"]

vegetables=vegetable1+vegetable2
print(vegetables)

#you cannot merge a list with a number or a string. lists only merge with lists.
#we can merge lists via + but it is not always the best option since we mşght want to add individual items from variable lists so we use list methods.
#list methods
#to append a item at the end of the row of a list, we use .append()

vegetables.append("corn")
print(vegetables)

#.insert(1,"item") method is used to insert an item to a specific index of a list.
vegetables.insert(1,"lettuce")
print(vegetables)

#.extend(variable) method extends and merges two differnt collection datas. and adds the last append list to the end of the row.

cars=["BMW","Mercedes","Skoda","Toyota","Nissan"]
hobbies=("Skiing","Surfing","Hiking","Swimming")

cars.extend(hobbies)
print(cars)

#to create a individual copy of a list we have the .copy() method

