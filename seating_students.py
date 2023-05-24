def seating_students(arr: list) -> int:
    if not arr:
        return 0
    rows = arr[0] // 2
    seats = [[] for _ in range(rows)]

    s = 0
    for i in range(rows):
        for _ in range(2):
            seats[i].append(s + 1 in arr[1:])
            s += 1

    c = 0
    for i in range(rows - 1):
        if not any(seats[i]):
            c += 1
        for j in range(2):
            if not seats[i][j] and not seats[i + 1][j]:
                c += 1
    if not any(seats[rows - 1]):
        c += 1

    return c


data = [12, 2, 6, 7, 11]
print(seating_students(data))
