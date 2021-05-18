#6. Write a python program to find the repeated items of a tuple.

tup = [2,3,4,5,3,4,2]
alist = list(tup)
from collections import Counter
result = dict(Counter(alist))
print(result)
