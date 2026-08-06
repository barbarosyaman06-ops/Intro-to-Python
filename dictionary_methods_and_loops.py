school={
  "name": "İTÜ",
  "location": "İstanbul",
  "QS_ranking": 279,
  "students": 20000,
  "departments": ["Engineering", "Architecture", "Business"],
  "year": 1773
}

for key_item,value_item in school.items():
    print(f"{key_item}-{value_item}")


school2=school.copy()
print(school2)
school["year"]=2026
print(school2)

myFriends={
    "friend1": {
        "name": "Uras",
        "age": 20,
        "city": "İstanbul",
        "major": "Medicine"
    },
    "friend2": {
        "name": "yalın",
        "age": 20,
        "city": "İstanbul",
        "major": "bussiness"
    }  
}

print(myFriends["friend1"]["name"])

for outer_key,outer_value in myFriends.items():
    print(f"{outer_key}")
    for inner_key,inner_value in outer_value.items():
        print(f"{inner_key}-{inner_value}")


myKeys=["key1","key2","key3"]
myValue=7
result=dict.fromkeys(myKeys,myValue)
print(result)

result2=school.setdefault("Erasmus",True)
print(result2)
print(school)