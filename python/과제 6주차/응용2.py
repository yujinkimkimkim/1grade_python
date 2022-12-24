N = input()

num_list = []

for i in range(1,len(N)+1):
    if(len(N) % i == 0):
        num_list.append(i)

for i in num_list:
    C = i
    R = len(N) // C
    if(R<=C and R*C==len(N)):
        break

arr = [[0 for j in range(C)] for i in range(R)]
cnt = 0
for i in range(C):
    for j in range(R):
        arr[j][i] = N[cnt]
        cnt += 1

temp =[]

for i in range(R):
    for j in range(C):
        temp.append(arr[i][j])

array = ''.join(temp)
print(array)

