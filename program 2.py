# 2. Write a python program to find the first repeated character in a given string.
def firstRepeatedChar(str):
    h = {}
    h = str[:1]
    for ch in str:
        if ch in h:
            return ch;
        else:
            h[ch] = 0
    return '\0'
print(firstRepeatedChar("character"))