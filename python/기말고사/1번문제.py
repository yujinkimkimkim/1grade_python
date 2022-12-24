class AirConditioner:
    temp = 0
    check = False

    def on(self):
        self.check = True
    def off(self):
        self.check = False
    def input_temp(self, num):
        if(self.check == True):
            self.temp = num
    def plus_temp(self):
        if(self.check == True):
            self.temp += 1
    def minus_temp(self):
        if (self.check == True):
            self.temp -= 1
    def print_temp(self):
        print(self.temp)

a = AirConditioner()
a.on()
a.input_temp(20)
a.plus_temp()
a.minus_temp()
a.print_temp()

a.off()
a.minus_temp()
a.print_temp()

