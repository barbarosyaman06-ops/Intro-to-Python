text="The price is only {price:.2f} turkish lira!"
text1="My school is located at {location}, I am {name}, and i am {age}.".format(location="İTÜ",name="Barbaros",age=20)
print(text.format(price=70.12944514))
print(text1)
also="My name is {0},and i am {1}.".format("Barbaros",20)
print(also)