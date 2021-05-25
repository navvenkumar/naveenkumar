#10.Write a python program to convert a list into a nested dictionary of keys.
list1 = [20,30,10,22]
new_dict = current = {}
for name in list1:
    current[name] = {}
    current = current[name]
print(new_dict)
