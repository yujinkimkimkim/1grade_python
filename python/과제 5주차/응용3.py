import sys

read = sys.stdin.readline

n, m = map(int, read().split(' '))

answer = 'Yes'

for _ in range(m):
    if answer == 'Yes':
        i = int(read())
        k = list(map(int, read().split(' ')))
        for j in range(i-1):
            if k[j] < k[j+1]:
                answer = 'No'
                break
    else:
        break

print(answer)