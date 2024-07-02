square = [[4,3,8],[9,5,1],[2,7,6]]

# print(square[0][0]+square[1][0]+square[2][0])

def magic_square(matrix):
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        return False

    magic_sum = sum(matrix[0])

    for row in matrix:
        if sum(row) != magic_sum:
            return False

    for col in range(n):
        if sum(matrix[row][col] for row in range(n)) != magic_sum:
            return False

    if sum(matrix[i][i] for i in range(n)) != magic_sum:
        return False

    if sum(matrix[i][n - 1 - i] for i in range(n)) != magic_sum:
        return False

    return True


if (magic_square(square)):
    print("Magic Square")
else:
    print("Not Magic Square")