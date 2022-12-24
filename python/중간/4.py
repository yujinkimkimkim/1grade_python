max = int(input('생성할 큐의 크기를 설정해주세요 >> '))
Queue = []

def data_In(x):
    Queue.append(x)
    print('현재 큐 현황: ', Queue )

def data_pop():
    p =Queue.pop(-1)
    print('현재 큐 현황: ', Queue, '출력된 데이터: ',p)

while (True):
    text = list(input('명령을 입력하세요 >> ').split())
    
    if(text[0] == 'exit'):
        break

    elif (text[0]=='입력'):
        if(len(Queue)==max):
            print('오버플로우 입니다! 큐가 꽉찼습니다')
        else:
            data_In(text[1])

    elif (text[0]=='출력'):
        if(len(Queue)==0):
            print('언더플로우 입니다! 큐가 비었습니다')
        else:
            data_pop()

    
