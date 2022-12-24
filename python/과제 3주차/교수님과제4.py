class Grade:
    name = ""
    kor = 0
    mat = 0
    eng = 0

    def __init__(self, name, kor, mat, eng):
        self.name = name
        self.kor = kor
        self.mat = mat
        self.eng = eng

    def score(self, arr):
        if arr == 'kor':
            print(self.name, '의 국어 점수는 ', self.kor)
        if arr == 'eng':
            print(self.name, '의 영어 점수는 ', self.eng)
        if arr == 'mat':
            print(self.name, '의 수학 점수는 ', self.mat)

    def average(self):
        sum = 0
        sum = self.kor + self.eng + self.mat
        print(self.name, '의 평균 점수는 ', round((sum/3),2))

    def __del__(self):
        print(self.name, ': 학생 객체는 삭제되었습니다')

p1 = Grade("kim", 60, 80, 65)
p1.score('kor')
p1.average()
del(p1)
        

