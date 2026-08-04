schools={"Harvard", "MIT", "Stanford", "Yale"}

schools.add("Princeton")
print(schools)

provinces1={"Ontario", "Quebec", "British Columbia"}
provinces2={"Alberta", "Manitoba", "Saskatchewan"}
provinces3={"Nova Scotia", "New Brunswick", "Prince Edward Island"}
provinces4={"Newfoundland and Labrador", "Northwest Territories", "Nunavut", "Yukon"}

provinces1.update(provinces2,provinces3, provinces4)
print(provinces1)

furniture={"table", "chair", "sofa"}
furniture1={"bed", "dresser", "nightstand"}
furniture2={"couch", "recliner", "ottoman"}

furniture |= furniture1 | furniture2
print(furniture)

new_set={"apple", "banana", "cherry"}
new_set.remove("banana")
print(new_set)

new_set.discard("banana")
print(new_set)

remove_item=new_set.pop()
print(remove_item)

homes={"apartment", "condo", "house", "townhouse"}
homes1=["apartment", "cabin", "cottage", "duplex"]

result=homes.intersection(homes1)
print(result)

homes.intersection_update(homes1)
print(homes)

setNumber1={1, 2, 3, 4, 5}
setNumber2={4, 5, 3, 7, 5}
setNumber3={1, 2, 3, 4, 5, 6, 7, 8}

result1=setNumber1.difference(setNumber2)
print(result1)



