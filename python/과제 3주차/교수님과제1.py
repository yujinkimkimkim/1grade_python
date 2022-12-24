class Human:
    humanName = ""
    humanAge = 0
    humanSex = ""
    def __init__(self, name, age, sex):
        self.humanName = name
        self.humanAge = age
        self.humanSex = sex

    def setHumaninfo(self, name, age, sex):
        self.humanName = name
        self.humanAge = age
        self.humanSex = sex
    
    def printInfo(self):
        print(self.humanName, self.humanAge, self.humanSex)

kim = Human("김하성", 27, "남")
kim.printInfo()

unknown = Human("모름", 0 , "모름")
unknown.setHumaninfo("산타할아버지", 100 , "남")
unknown.printInfo()

