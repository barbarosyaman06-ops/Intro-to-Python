#tupples are used to store multiple items in a single variable. They are similar to lists, but they are immutable, meaning that once a tuple is created, its values cannot be changed. Tuples are defined by enclosing the items in parentheses () and separating them with commas.

fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print(fruits)  # Output: ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango')

print(len(fruits))  # Output: 7

fruits1=("grape")
fruits2=("grape",)

print(type(fruits1))  # Output: <class 'str'>
print(type(fruits2))  # Output: <class 'tuple'>

complex_tupple=(1,2,4,"Hello",True,3.14,[1,2,3],(4,5,6),{"name":"John","age":30})
print(complex_tupple)  # Output: (1, 2, 4, 'Hello', True, 3.14, [1, 2, 3], (4, 5, 6), {'name': 'John', 'age': 30})