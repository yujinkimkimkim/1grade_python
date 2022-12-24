class Line:
    length = 0

    def __init__(self, value):
        self.length = value
        print(self.length, "길이의 선이 생성되었습니다.")

    def __add__(self, other):
        print("두 선의 합 :", self.length + other.length)

    def __del__(self):
        print(self.length, "길이의 선이 제거되었습니다.")

    def __lt__(self, other):
        if (self.length < other.length):
            return True
        else:
            return False

line1 = Line(10)
line2 = Line(5)
line1 + line2

if (line1 < line2):
    print("선2가 더 깁니다.")
    del(line1)
else:
    print("선1이 더 깁니다.")
    del(line2)

