num = int(input())

if(num>=28):
    sum = num + 1 + 2 + 3 + 4 + 5 + 6
    result = sum // 7
    if(sum%7!=0):
        result += 1
    print(result)
else:
    for i in range(1, 8):
        if num <= sum(range(1, i + 1)):
            print(i)
            break
