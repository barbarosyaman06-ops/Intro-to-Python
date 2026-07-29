#fibonacci series algorithm

entered_number=int(input("Please enter a ceiling number: "))

fibonacci=[]
first=0
second=1

#if we want to operate with multiple numbers but dont need a index from for loop, we use a underscore after for


for _ in range(entered_number):
    fibonacci.append(first)
    temporary=first+second
    first=second
    second=temporary
print(fibonacci)


#this temp,first and second variables are used in swapping in lists and series
#this helps us memorize the previous variable
#we say lets make the second variable temporary which is first+second, and
#we want to make first variable equal to second so we type first=second
#an at last we wanr to remember the temp and define second=temp so which sucessfully
#swaps the data to new one in fibonacci series
#this is also used in queues

#importance of temp variable!

     