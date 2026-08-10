def sum_recursion(n):
    if(n>0):
      result=n+sum_recursion(n-1)
    else:
      result=0
    return result

print(sum_recursion(7))

