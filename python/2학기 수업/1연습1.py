class rabbit:
    shape = ""
    xPos = 0
    yPos = 0
    
    def __init__(self, value):
        self.shape = value

    def rab(self, x, y):
        self.xPos += x
        self.yPos += y
        print('토끼의 현재 위치는 (', self.xPos,',', self.yPos,') 입니다')

while(True):
    rabbit1 = rabbit('원')
    x = int(input('토끼가 이동할 X좌표 >>'))
    y = int(input('토끼가 이동할 y좌표 >>'))
    rabbit1.rab(x, y)

