x = int(input('숫자를 입력해주세요 :'))

list = []

def fe(a):
    sum = 0
    for i in range(1,x+1):
        if i % 4 != 0 and i % 8 != 0:
            list.append(i)
            sum = sum + i
    return sum

sum = fe(x)

print('4 또는 8의 배수가 아닌 수는 다음과 같습니다')

for i in range(len(list)):
    print(list[i], ' ', end='')
    
print()
print('다음 수들의 합은' , sum, '입니다')

