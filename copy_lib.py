import copy

#we use copy lib and deepcopy methods to copy complex sublisted lists

list1=[[1,2],[3,4]]
list2=copy.deepcopy(list1)

list2[0][0]=70
list2[0][1]=64
list2[1][0]=54
list2[1][1]=24

print(list1)
print(list2)
