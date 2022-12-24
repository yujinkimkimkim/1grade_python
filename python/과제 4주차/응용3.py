num = int(input())

for i in range(num):
    arr = input()
    n = int(len(arr)**(1/2))
    x = len(arr)

    arr2 = []
    arr3 = []
    for j in range(n):
        for k in range(1,n+1):
            print(arr[x-n*k+j],end='')
            arr2.append(arr[x-n*k+j])
        print()
    for l in range(1,x+1):
        arr3.append(arr2[-l])
    arr3 = ''.join(s for s in arr3)
    print(arr3)


