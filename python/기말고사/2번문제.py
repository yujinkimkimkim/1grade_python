import pandas as pd

data = pd.read_csv("./diamonds.csv")
print(data.loc[0:4]) #5개 행 추출, data.head()도 0~4행 불러올 수 있음
print(data.head())

data_new = data.drop(['cut'], axis = 1) # axis = 1 이 열 기준으로 한다는 것 의미함
print(data_new.head())

data_price = data['price']
data_price = data_price.sort_index(ascending=False)
print(data_price)

data_24 = data[['carat', 'cut']]
data_24 = data_24.loc[2:4]
print(data_24)

