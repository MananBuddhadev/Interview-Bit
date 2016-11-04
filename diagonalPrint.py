def diagonal(a):
    output = [[]]*(2*len(a[0])-1)
    x=[0]*(2*len(a[0])-1)

    for i in range((2*len(a[0])-1)):
        x[i]=[]
    if len(a) is 1:
        return a

    for i in range(len(a[0])):
        for j in range(len(a[0])):
            x[i+j].append(a[i][j])

    return x

def main():
    a=[[1,2],[3,4]]
    print(diagonal(a))

if __name__ == '__main__':
    main()