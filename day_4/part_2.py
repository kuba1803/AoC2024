import string

sum = 0

word = "MAS"

srcMatrix = []
maskMatrix = []


def find_word(matrix, x, y, word, maskMatrix):
    if (matrix[y][x] != "A"):
        return False

    if not((matrix[y - 1][x - 1] == "M" and matrix[y + 1][x + 1] == "S") or (
            matrix[y - 1][x - 1] == "S" and matrix[y + 1][x + 1] == "M")):
        return False
    if not ((matrix[y + 1][x - 1] == "M" and matrix[y - 1][x + 1] == "S") or (
            matrix[y + 1][x - 1] == "S" and matrix[y - 1][x + 1] == "M")):
        return False

    for idx in range(len(word)):
        maskMatrix[y - 1 + idx][x - 1 + idx] = matrix[y - 1 + idx][x - 1 + idx]
        maskMatrix[y + 1 - idx][x - 1 + idx] = matrix[y - 1 + idx][x - 1 + idx]

    return True


with open('input_file.txt') as f:
    for line in f:
        srcMatrix.append(list(filter(lambda x: x in string.ascii_letters, line)))

    for i in range(len(srcMatrix)):
        maskMatrix.append(["."] * len(srcMatrix[0]))

    for y in range(1, len(srcMatrix) - 1):
        for x in range(1, len(srcMatrix[i]) - 1):
            if (find_word(srcMatrix, x, y, word, maskMatrix)):
                sum += 1

for line in srcMatrix:
    print(line)

for line in maskMatrix:
    print(line)

print(sum)
