import string

sum = 0

word = "XMAS"

srcMatrix = []
maskMatrix = []

def find_word( matrix, x, y, word, v_x, v_y, maskMatrix ):
    if( v_x == 0 and v_y == 0 ):
        return False
    if( v_x == 1 and x + len(word) > len(matrix[0]) ):
        return False
    if( v_y == 1 and y + len(word) > len(matrix) ):
        return False
    if( v_x == -1 and x - len(word) + 1 < 0 ):
        return False
    if( v_y == -1 and y - len(word) + 1 < 0 ):
        return False

    for idx in range( len(word) ):
        if( word[idx] != matrix[ y + v_y*idx ][ x + v_x*idx ] ):
            return False

    for idx in range( len(word) ):
        maskMatrix[ y + v_y*idx ][ x + v_x*idx ] = matrix[ y + v_y*idx ][ x + v_x*idx ]

    return True



with open('input_file.txt') as f:
    for line in f:
        srcMatrix.append(list(filter(lambda x: x in string.ascii_letters, line)))

    for i in range(len(srcMatrix)):
        maskMatrix.append(["."] * len(srcMatrix[0]))

    for y in range(len(srcMatrix)):
        for x in range(len(srcMatrix[i])):
            for v_y in range(-1,2):
                for v_x in range(-1,2):
                    if( find_word( srcMatrix, x, y, word, v_x, v_y, maskMatrix ) ):
                        sum += 1



for line in srcMatrix:
    print(line)

print("")

for line in maskMatrix:
    print(line)

print(sum)
