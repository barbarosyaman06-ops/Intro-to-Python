#isdigit returns a boolean value if the string is a digit or not.
text="14664123"
result=text.isdigit()
print(result)
#isidentifier returns a boolean value if the string contains general letters, numbers, and underscores but does not start with a number.
#islower returns a boolean value if the string is in lowercase or not.
#isupper returns a boolean value if the string is in uppercase or not.
#isnumeric returns a boolean value if the string is a number or not. does not include negative numbers or decimal numbers.
#isprintable returns a boolean value if the string is printable or not. it returns false for escape characters like \n, \t, etc.
#isspace returns a bollean value which checks if the string contains only whitespace characters or not.
#istitle indicates if the every string in the text starts with a capital letter or not. it returns a boolean value.
#join is a method that joins the elements of an iterable with a string separator. it returns a string.
Names=("Barbaros","Ahmet","Mehmet","Ali")
result="_".join(Names)
print(result)
myInfo={"name":"Barbaros","age":20}
mySeperator=" | "
result=mySeperator.join(myInfo["name"])
print(result)
text="strawberry"
result=text.ljust(20,"*")
print(result,"is my favourite fruit")
#strip,lstrip,rstrip are methods that remove the whitespace characters from the string. lstrip removes the whitespace characters from the left side of the string, rstrip removes the whitespace characters from the right side of the string, and strip removes the whitespace characters from both sides of the string.
text="...Hello Brother..."
result=text.strip(".")
print(result)

text2="Hello Python"
result2=text2.maketrans("H","J")
print(text2.translate(result2))

#ps dictionary is a variable that helps us to translate multiple characters at once.
MyDict={80:84,108:65,82:72}
text3="Play Hard"
result3=str.maketrans(MyDict)
print(text3.translate(result3))

#maketrans is a method wtih 3 paramaters. x and y are the characters that we want to replace and z is the characters we want to erase.

text3="Hello World"
x="He"
y="We"
z="o"
result3=str.maketrans(x,y,z)
print(text3.translate(result3))

#.partition is a method that splits the string into 3 parts.
text4="I want to surf as a hobby"
result=text4.partition("surf")
print(result)

#replace is a method that replaces a specific character or string with another character or string. it returns a string.
text5="I want to surf as a hobby,surf,surf,surf,surf,surf"
result5=text5.replace("surf","play football")
print(result5)
#also replace can be used to replace a specific number of elements such as the first 2 elements of a string.
result6=text5.replace("surf","play football",3)
print(result6)