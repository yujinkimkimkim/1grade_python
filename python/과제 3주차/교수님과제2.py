class Calculator:
    num = 0
    tu = ()

    def __init__(self, *x):
        self.tu = x

    def sum1(self):
        self.num = 0
        for a in self.tu:
            self.num += a
        return self.num

    def avg(self):
        self.num = 0
        cnt = 0
        for b in self.tu:
            self.num += b
            cnt += 1
        return self.num/cnt
            

cal_1 = Calculator(1,2,3,4,5)
print(cal_1.sum1())
print(cal_1.avg())
