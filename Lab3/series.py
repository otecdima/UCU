number = int(input())

firstnumber = "1/2"
print(firstnumber, end="")

for i in range(1, number):
    if i % 2 != 0:
        print(' - ' + str(i*2+1) + '/' + str(i*2+2), end="")
    else:
        print(' + ' + str(i*2+1) + '/' + str(i*2+2), end="")
print()
    