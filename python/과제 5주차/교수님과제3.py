def three_multi(num):
    try:
        if (num % 3 == 0):
            print('{}은 3의 배수가 맞습니다'.format(num))
        else:
            raise InvalidNumberException(num)
    except InvalidNumberException as err:
        print(err)

class InvalidNumberException(Exception):
    def __init__(self,num):
        super().__init__("{}는 3의 배수가 아닙니다. InvalidNumberException을 발생시킵니다.".format(num))

n = int(input('3의 배수를 입력하세요 : '))
three_multi(n)