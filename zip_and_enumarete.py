fruits=["apple","pear","cherry","melon","watermelon"]



for index,item in enumerate(fruits):
    print(f"{index}-{item}")


#enumarate and zips are used for declusttering datas and storing them in a tupple. when 
#used simeltanously with list method. It is generally used to craft couples with words
#The system itself is based on key and value logic.



names=["Barbarsos","Yiğit","Uras","Yağız"]
ages=[20,46,20,19]

print(list(zip(names,ages)))