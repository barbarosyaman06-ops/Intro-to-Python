#for loops
artifical_intelligences=["ChatGPT","Grok","Claude","DeepSeek","Gemini","Kumru"]

i=0
for item in artifical_intelligences:
    print(i,".index=",item)
    i+=1

#lists,tuuples,dictionaries,sets are iterable and iteration means repeated actions.

myNumbers=(13,45,66,79,10,24,52,17)

for i in myNumbers:
    print(i)

#you can even print strings in for loops.

text="Python"

for letter in text:
    print(letter)

cars=["BMW","Peugot","Dacia","Hyundai","Honda","Nissan"]

for x in cars:
    if(x=="Peugot"):
      continue
    print(x)

#the order of the methos and command blocks are very important which changes the whole purpose of the command.
