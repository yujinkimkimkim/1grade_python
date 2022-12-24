import random
check = 0 #승부 판가름 위한 거
p = []
p_list = [0,1,2,3,4,5,6,7,8] #승부판 배열 리스트인데 선택될 때마다 없애려고
for i in range(9):
    p.append('.')

def In(x):
    arr_num = 0
    p[x] = 'O'
    for i in range(3):
        for j in range(3):
            print(p[arr_num], '  ', end='')
            arr_num += 1
        print()

def Match():
    if (p[0] and p[1] and p[2] == 'O')or(p[0] and p[1] and p[2] == 'X'):
        check = 0
    if (p[3] and p[4] and p[5] == 'O')or(p[3] and p[4] and p[5] == 'X'):
        check = 0
    if (p[6] and p[7] and p[8] == 'O')or(p[6] and p[7] and p[8] == 'X'):
        check = 0
    if (p[0] and p[3] and p[6] == 'O')or(p[0] and p[3] and p[6] == 'X'):
        check = 0
    if (p[1] and p[4] and p[7] == 'O')or(p[1] and p[4] and p[7] == 'X'):
        check = 0
    if (p[2] and p[5] and p[8] == 'O')or(p[2] and p[5] and p[8] == 'X'):
        check = 0
    if (p[0] and p[4] and p[8] == 'O')or(p[0] and p[4] and p[8] == 'X'):
        check = 0
    if (p[2] and p[4] and p[6] == 'O')or(p[2] and p[4] and p[6] == 'X'):
        check = 0

first = True
def computer_first(x):
    p_list.pop(x) #선택된 칸 pop해서 computer가 못 고르게 하려고
    if (4 in p_list):
        p[4] = 'X'
    else:
        choice = random.choice(p_list)
        p[choice] = 'X'

def computer(x):


print('  참고표')
print('1   2   3')
print('4   5   6')
print('7   8   9')

while (check):
    num = int(input('놓고 싶은 곳을 위에 표을 참고하여 입력해주세요 >>'))
    In(num-1)
    if first:
        computer_first(num-1)
        first = False
    else:
        computer(num-1)    
    