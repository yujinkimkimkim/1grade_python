with open('baseball.txt', 'r', encoding='utf-8') as file:
    try:
        num = int(input('출력할 라인 수는? : '))

        if(num <= 10 and num >= 1):
            for i in range(num):
                line = file.readline()
                print(line)
        else:
            raise Exception("입력 라인 수는 1~10까지 입니다")
    except ValueError:
        print('입력은 정수로만 해주세요')
    except Exception as err:
        print(err)
