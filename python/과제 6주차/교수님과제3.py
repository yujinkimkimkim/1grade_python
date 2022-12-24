import numpy as np

def nearest_value(X, target):
    temp = target - X
    temp = abs(temp)
    temp_min = min(temp)
    temp_idx = np.where(temp == temp_min)

    print('가장 인접한 값 :', X[temp_idx])

X = np.array([1,2,3,4,5,6,7])
target = 4.3
nearest_value(X, target)


