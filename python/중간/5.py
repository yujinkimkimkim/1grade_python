import random
ground = 0
Me = False
Computer = False
board = [[" "for a in range(3)]for b in range(3)]

for i in range(3):
    print(" ",board[i][0],"| ",board[i][1],"| ",board[i][2])
    if (i != 2):
        print("----|----|----")

def In(x,y):
    arr_x = 0
    arr_y = 0
    board[x][y] = 'O'
    for i in range(3):
        print(" ",board[i][0],"| ",board[i][1],"| ",board[i][2])
        if (i != 2):
            print("----|----|----")

def computer():
   while(True):
        i = random.randrange(0,3)
        j = random.randrange(0,3)
        if(board[i][j] == ' '):
            board[i][j] = 'X'
            print('컴퓨터 차례입니다 >>')
            for i in range(3):
                print(" ",board[i][0],"| ",board[i][1],"| ",board[i][2])
                if (i != 2):
                    print("----|----|----")
            break
        if(ground >= 9):
            break

def check_Me():
    if (board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O'):
        return True
    elif (board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O'):
        return True
    elif (board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O'):
        return True
    elif (board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O'):
        return True
    elif (board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O'):
        return True
    elif (board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O'):
        return True
    elif (board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O'):
        return True
    elif (board[2][0] == 'O' and board[1][1] == 'O' and board[0][2] == 'O'):
        return True

def check_Computer():
    if (board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X'):
        return True
    if (board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X'):
        return True
    if (board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X'):
        return True
    if (board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X'):
        return True
    if (board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X'):
        return True
    if (board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X'):
        return True
    if (board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X'):
        return True
    if (board[2][0] == 'X' and board[1][1] == 'X' and board[0][2] == 'X'):
        return True

while(True):
    print(">> 놓을 곳의 좌표를 입력하세요 >>", end='')
    x, y = input().split(',')
    x = int(x)
    y = int(y)

    In(x-1,y-1)
    ground = ground + 1

    computer()
    ground = ground + 1

    Me = check_Me()
    if(Me):
        print('축하드립니다 당신의 승리입니다~!')
        break
    Computer = check_Computer()
    if(Computer):
        print('컴퓨터의 승리입니다 ㅠㅠ')
        break
    
    if (ground == 10):
        print('비겼습니다!')
        break