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
#we can merge lists via + but it is not always the best option since we might want to add individual items from variable lists so we use list methods.
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

#we cant just equate two differnt lists and operate methods on one. the reason is that equated lists indicate the same shared ram storage and they cant act like individuals.
#so to solve this we create a individual copy of a list via .copy() method
#copy

clothes=["T-shirt","Jorts","Jeans","Cap","Watch"]
new_clothes=clothes.copy()

new_clothes.append("Shirt")

print(new_clothes)
print(clothes)

#we can also use the already existing methods like list() to operate with a individual list
#list(list_name)

countries=["Türkiye","USA","England"]
new_countries=list(countries)

new_countries.append("Greece")

print("countries=",countries)
print("new countries=",new_countries)

#we can also use the slice operator [:] to copy and operate troughout the lists.

provinces=["Istanbul","Muğla","Erzurum","Aydın","Datça"]
new_provinces=provinces[:]

new_provinces.append("Kocaeli")

print("Provinces=",provinces)
print("New Provinces=",new_provinces)

