class Car():
    model = ""
    color = ""
    b = 0
    def __init__(self, m, c, b):
        self.model = m
        self.color = c
        self.b = b
    def displayCar(self):
        print("모델명 :{}, 색상: {}, 배기량: {}".format(self.model,self.color,self.b))

class ElectricCar(Car):
    type = ""
    def __init__(self, m, c, t):
        self.model = m
        self.color = c
        self.type = t
    def displayCar(self):
        print("모델명 :{}, 색상: {}, 배터리 타입: {}".format(self.model,self.color,self.type))

car = Car("Samsung SM%","black",2000)
car.displayCar()
elec_car = ElectricCar('Tesla Model 3', ' black', 'Lithium')
elec_car.displayCar()