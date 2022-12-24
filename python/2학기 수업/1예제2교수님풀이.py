class Rabbit:
    shape = ""
    xPos = 0
    yPos = 0

    def __init__(self, value):
        self.shape = value
    
    def goto(self, x, y):
        self.xPos = x
        self.yPos = y

    def print_describe(self):
        print("토끼의 모양은" + self.shape + ", x좌표는: " + str(self.xPos) + ", y좌표는: " + str(self.yPos))

    def __del__(self):
        print("이제", self.shape, "는 자유에요~~")

    def __add__(self, other):
        print("객체", self.shape, "와", other.shape, "가 친구가 되었습니다.")


#rabbit1 = Rabbit()
#rabbit1.shape = "원"
#rabbit1.xPos = 100
#rabbit1.yPos = 100
#rabbit1.print_describe()

#rabbit2 = Rabbit()
#rabbit2.shape = "삼각형"
#rabbit2.xPos = -100
#rabbit2.yPos = 100
#rabbit2.print_describe()

#rabbit3 = Rabbit()
#rabbit3.shape = "토끼"
#rabbit3.xPos = 0
#rabbit3.yPos = -100
#rabbit3.print_describe()

#rabbit1 = Rabbit()

#while (1) :
#    move_x = input("토끼가 이동할 x 좌표 ==> ")
#    move_y = input("토끼가 이동할 y 좌표 ==> ")
#    rabbit1.goto(int(move_x), int(move_y))
#    print("토끼의 현재 위치는 (" + str(rabbit1.xPos) + "," + str(rabbit1.yPos)
#          + ")")

rabbit1 = Rabbit("원")
#print('rabbit1의 모양:', rabbit1.shape)

rabbit2 = Rabbit("삼각형")
#print('rabbit2의 모양:', rabbit2.shape)

rabbit3 = Rabbit("토끼")
#print('rabbit3의 모양:', rabbit3.shape)

rabbit1 + rabbit2
rabbit2 + rabbit3
