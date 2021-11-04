x, y = 5, 5

for i in range (1, x):
    if i < 3:
      print ("i less three", end=" ")
    for j in range (i, y):
        if (i + j) % 3 == 0:
          print (i, j, end=" ")