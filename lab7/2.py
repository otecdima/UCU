string1 = "NACHOS 1 N AA1 CH OW0 Z"
string2 = "NACHOS 2 N AE1 CH OW0 Z"

string.split()
# string.split(':')
word = string.split(" ")[0]
number = int(string.split(" ")[1])
pronunciation = string.split(" ")[2:]
print(string)
print(word)
print(number)
print(pronunciation)
