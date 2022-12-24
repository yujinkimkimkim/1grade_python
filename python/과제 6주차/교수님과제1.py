import numpy as np

arr = [[0 for i in range(10)] for j in range(10)]

for i in range(10):
    arr[i] = np.random.rand(10)*100

arr = np.round_(arr)

print(arr)
print(int(np.max(arr)))
print(int(np.min(arr)))
