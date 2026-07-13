text="I might fly to Cologne next week"
result=text.partition("Cologne")
print(result)
print(type(result))
text1="I can watch reels all day,reels are so addictive"
result1=text1.rpartition("reels")
print(result1)
#.find helps us to locate  the index of a specific character or string in a string.
#.rfind helps us locater tje rightmost index or string in a string.
#.index and rindex are very similar with find and rfind but they raise a value error.
#.split is a method that splits the string to parts based on a character.
text2="Welcome everyone, I hope you are doing well, I am doing well too, thanks"
result2=text2.split(",",)
print(result2)
#.splitlines functions similarly to split but it splits the string based on the line.
text3="Hello everyone\nI hope you are doing well\nI am doing well too\nthanks"
result3=text3.splitlines(True)#normally the index is False but if one wants to keep it we input True.
print(result3)
#.zfill is a method that fills the string with zeros from left to right. might be useful for lockers or passwords.
text4="12"
result4=text4.zfill(10)#the whole number will be 10 digits long. 
print(result4)
