#1.Write a python program to remove the nth index character from a nonempty string
str1 = "program"
index = input('Enter the index value:')
index = int(index)
str = str1[0:index]+str1[index+1:]
print(str)