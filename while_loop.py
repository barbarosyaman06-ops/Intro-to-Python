#while loop

increment=1

while (increment<=7):
    print(increment,"-Pyhton")
    increment+=1
    if(increment==5):
        break
print("Done")

#end=" " helps to sort the variable in a row
#there are break and continue statements that acts like a control station in a
#ongoing loop

#if reader comes across a continue key word it does not proceed and reads the 
#previous loops over and over again. We use continue to bypass a certain command
#block

#if reader come across a brak key word, it will brak from the loop and read the 
#upcoming commands.

#we can use else key word to escape from loops as well



#while loop with previous list data

MyNumbers=[12,16,24,66,89,56,43]

i=0
while (i<len(MyNumbers)):
    print(MyNumbers[i])
    i+=1



