arr = input().split('|')

jang = 0
dan = 0
dan_ = ['A','D','E']
jang_ = ['C', 'F', 'G']

for i in arr:
    if(i[0] in dan_):
        dan += 1
    elif(i[0] in jang_):
        jang += 1

if(jang > dan):
    print('C-major')
elif(dan > jang):
    print('A-minor')
else:
    a = arr[-1]
    if (a[-1] in dan_):
        print('A-minor')
    elif (a[-1] in jang_):
        print('C-major')

