import math

N = int(input())

if N == 0:
    print('NO')
else:
    for i in range(27, -1, -1):
        if (N >= math.factorial(i)):
            N -= math.factorial(i)
        if N == 0:
            break
    print('YES' if N==0 else 'NO')