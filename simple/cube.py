def coloring(ls):
    for z in range(len(ls)):
        for y in range(len(ls[z])):
            for x in range(len(ls[z][y])):
                if (
                    z == 0 or z == len(ls) - 1 or
                    y == 0 or y == len(ls[z]) - 1 or
                    x == 0 or x == len(ls[z][y]) - 1
                ):
                    ls[z][y][x] = 1
                else:
                    ls[z][y][x] = 0

matrix = [
            [
                [5, 5, 5],
                [5, 5, 5],
                [5, 5, 5]
            ],
            [
                [5, 5, 5],
                [5, 5, 5],
                [5, 5, 5]
            ],
            [
                [5, 5, 5],
                [5, 5, 5],
                [5, 5, 5]
            ]
        ]

coloring(matrix)

for i in range(len(matrix)):
    print("{}th layer:".format(i+1))
    for j in matrix[i]:
        for k in j:
            print(k, end=' ')
        print()
