power = int(input())
number = 5 ** power
hemmingnumber = 0

binnumber = bin(number)

for i in range (len(binnumber)):
    if number >> i & 1:
        hemmingnumber = hemmingnumber + 1


if hemmingnumber % 2:
    type_num = "odious"
else:
    type_num = "evil"

print(f"Number {number} is {type_num} number. Its hamming weight is {hemmingnumber}.")
 


