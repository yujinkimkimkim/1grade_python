arr = list(input('명령을 입력하세요 >>').split(', '))

x = 0
y = 0

for i in arr:
    if (i[0]=='U'):
        y = y + int(i[1:])
    elif (i[0]=='D'):
        y = y - int(i[1:])
    elif (i[0]=='L'):
        x = x - int(i[1:])
    elif (i[0]=='R'):
        x = x + int(i[1:])
    else:
        print('알 수 없는 명령이 존재합니다')

print('로봇의 현재 좌표는 현재:',x , ', ', y, '입니다.')
