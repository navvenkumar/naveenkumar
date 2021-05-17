#3.Write a python program to find the second smallest number in a list
lst = [1,63,48,55,22]
output = min(lst)
lst.remove(output)
result = min(lst)
print(result)