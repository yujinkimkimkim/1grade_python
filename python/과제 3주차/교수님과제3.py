class Circle:
    r = 0
    
    def __init__(self, value):
        self.r = value

    def calcPerimeter(self):
        print('원의 둘레는 ', round((self.r * 2 * 3.14), 2))

    def calcArea(self):
        print('원의 면적 ',self.r * self.r * 3.14)

num = int(input('반지름을 입력하세요>>'))
cir1 = Circle(num)
cir1.calcPerimeter()
cir1.calcArea()

