def warshall(a):
    assert(len(row) == len(a) for row in a)
    n = len(a)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                a[i][j] = a[i][j] or(a[i][k] and a[k][j])
        print(f"Крок {k + 1}: {a}")
    return f"\nРезультат: {a}"

#===<ENTER MATRIX>===#

print(warshall([
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    ]))
