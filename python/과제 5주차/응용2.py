num,arr = map(int,input().split(' '))

word_list = []
cnt = 0
result = 0

for i in range(num):
    word_list.append(input())

for k in range(num-1):
    result = 0
    for j in range(1,arr+1):
        if word_list[k][:j] == word_list[k + 1][arr-j:]:
            result = 1
            break

        if word_list[k][arr-j:] == word_list[k + 1][:j]:
            result = 1
            break

    if result == 0:
        print(0)
        exit(0)
print(1)