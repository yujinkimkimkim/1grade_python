
try:
    while(True):
        list1 = list(map(float,input().split()))

        if(list[0] == 0):
            break

        sum = list1[0]
        cnt = 0
        while(True):
            sum = sum + sum * list1[1]*0.01
            cnt += 1
            if(sum >= list1[2]):
                break
                
        print(cnt)
        
except: exit()