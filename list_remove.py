applications=["Twitter","Instagram","Facebook","Youtube","LinkedIn","Reddit","Github"]

applications.remove("Twitter")

print(applications)

#.remove("name_of_item") removes the corresponding item from the list.
#important if the list has 3 similar items remove method only removes the first one from the list
#.pop(index) method pops the specified item of the list and if no index is given it will extract the last item of the list.


animals=["cat","dog","bird"]

last_animal=animals.pop()

print(animals)
print(last_animal)

#we can also use "del" key word and specify a index to remove a item from the list.

games=["GOW","RDR2","GTAV","CyberPunk"]

del games[2]

print(games)

#.clear() method clears the items from the lists.

# games.clear()

# print(games)

#.index() returns the index specifier of a item from the list. If the list contains the same item more than once list returns only the first index specifier.

result=games.index("RDR2")

print(result)

#.count() method returns the amount of times that the same item has repeated in corresponding list.

myNumbers=["1","2","4","1","7","1","4","7","1"]

print(myNumbers.count("1"))