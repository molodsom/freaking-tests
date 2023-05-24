def matrix_spiral(m: list) -> list:
    def rotate(inp: list) -> list:
        return list(reversed(list(zip(*inp))))

    o = m[0] if m else []
    while len(m) > 1:
        m = rotate(m[1:])
        o += m[0] if m else []
    return o


matrix = [
    [10, 11, 12, 13],
    [14, 15, 16, 17],
    [18, 19, 20, 21],
    [22, 23, 24, 25]
]
print(matrix_spiral(matrix))
