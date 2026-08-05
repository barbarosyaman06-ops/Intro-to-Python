car={
  "brand": "TOGG",
  "model": "C-SUV",
  "country": "Turkey",
  "year": 2023
}

result=car.items()
print(result)
car["colors"]=["red", "white", "blue"]
print(car)


#we can also use the update() method to add new key-value pairs to the dictionary
car.update({"engine": "electric"})
print(car)

#pop pops the specified item from the dictionary
car.pop("country")
print(car)

#popitem pops the last item from the dictionary
car.popitem()
print(car)

#del car["model"] does the same thing as pop() but it does not return the value of the deleted item

del car["brand"]
print(car)

#clear() method removes all items from the dictionary
car.clear()
print(car)