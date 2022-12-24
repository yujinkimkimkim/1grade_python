n, m = map(int, input().split(' '))

p = 1
board = [int(input()) for _ in range(n)]
dice = [int(input()) for _ in range(m)]

for i in range(m):
    p = p + dice[i]
    if (p >= n):
        print(i+1)
        break
    p = p + board[p-1]
    if(p >= n):
        print(i+1)
        break

