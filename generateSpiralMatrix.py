def generateMatrix( A):
    top = 0
    left = 0
    count = 1
    right = A
    bottom = A
    direction = 0

    spiralMatrix = [[0 for column in range(A)] for column in range(A)]

    while (top < bottom):
        if direction is 0:
            for i in range(left, right):
                spiralMatrix[top][i] = count
                count += 1
            top += 1
            direction = 1

        if direction is 1:
            for i in range(top, bottom):
                spiralMatrix[i][right-1] = count
                count += 1
            right -= 1
            direction = 2

        if direction is 2:
            for i in range(right-1, left-1,-1):
                spiralMatrix[bottom-1][i] = count
                count += 1
            bottom -= 1
            direction = 3

        if direction is 3:
            for i in range(bottom-1, top-1,-1):
                spiralMatrix[i][left] = count
                count += 1
            left += 1
            direction = 0

    return spiralMatrix


def main():
    A=5
    generateMatrix(A)

if __name__ == '__main__':
    main()