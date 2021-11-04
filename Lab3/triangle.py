firstnumber = int(input())
sizeoftriangle = int(input())

for i in range (1, sizeoftriangle+1):
    for j in range (0, sizeoftriangle - i + 1):
        if j == sizeoftriangle-i:
            print(firstnumber + j) 
        else:
            print(firstnumber + j, end=" ")
    


