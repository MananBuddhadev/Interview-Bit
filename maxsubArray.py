def maxset(A):
    max_so_far = []
    max_ending_here = []

    for i in range(0, len(A)):
        if A[i] < 0:
            max_ending_here = []
        else:
            max_ending_here.append(A[i])

        sumNew = 0
        for element in max_ending_here:
            sumNew += element

        sumOld = 0
        for element in max_so_far:
            sumOld += element

        if (sumOld < sumNew):
            max_so_far = max_ending_here
        elif (sumOld == sumNew):
            if len(max_so_far) == 0:
                max_so_far = max_ending_here
            else:
                if max_ending_here:
                    if A.index(max_so_far[0]) > A.index(max_ending_here[0]):
                        max_so_far = max_ending_here

    return max_so_far

def main():
    A=[0, 0, -1, 0]
    x=maxset(A)
    print(x)

if __name__ == '__main__':
    main()