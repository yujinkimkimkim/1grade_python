# next = 1
# sum1 = 0
# pre = 1

# num = int(input())

# for i in range(num-2):
#     sum1 = pre + next
#     pre = next
#     next = sum1

# print((next + pre)*2 + next*2)

num = int(input())
arr = [0]*81
arr[0] = 4
arr[1] = 6

for i in range(2, num+1):
    arr[i] = arr[i-2] + arr[i-1]

print(arr[num-1])
