import math


def getRow(A):
    pascalArray = []

    spiralMatrix = [[0 for column in range(A)] for column in range(A)]
    pascal = str(int(math.pow(11, A)))

    for character in pascal:
        pascalArray.append(int(character))

    return pascalArray


def main():
    x=getRow(5)
    print(x)

if __name__ == '__main__':
    main()
