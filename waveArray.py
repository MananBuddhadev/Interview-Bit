def wave(A):
    if len(A) <= 1:
        return A

    A.sort()
    i=0
    while i < (len(A) - 1):
        if i // 2 == 0:
            if A[i] <= A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                i+=2

        else:
            if A[i+1] >= A[i]:
                A[i + 1], A[i] = A[i], A[i + 1]
                i+=2

    return A

def main():
    A=[5,1,3,2,4]
    print(wave(A))

if __name__ == '__main__':
    main()