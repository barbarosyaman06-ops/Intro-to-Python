car={
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "electric": False,
  "colors": ["red", "white", "blue"]
}

print(car["brand"], car["model"], car["year"])
print(car)
print(type(car))

person=dict(name="John", age=30, city="New York")

print(f"name: {person['name']}, age: {person['age']}, city: {person['city']}")

my_keys=car.keys()

print(my_keys)

car["year"]=2020
car["country"]="USA"

print(my_keys) 

my_new_value=car.values()

print(my_new_value)