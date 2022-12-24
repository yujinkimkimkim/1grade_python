num = int(input())
arr = input()

s_cnt = arr.count('S')
l_cnt = arr.count('L')

if 'L' in arr:
    print(int(s_cnt + l_cnt/2 + 1))
else:
    print(s_cnt)