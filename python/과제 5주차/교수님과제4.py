with open('yesterday.txt', 'r') as file:
    arr = file.read()
    num = arr.count('yesterday')
    print('"yesterday.txt"파일 안에는 총 {}번의 yesterday가 있습니다'.format(num))