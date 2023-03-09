import random

customer = 1
a = 0
while customer < 51: 
    time = random.randrange(1, 51)
    if time < 16 :
        print("[O]" + str(customer) +'번째 손님 (소요시간 : ' + str(time) + '분)')
        customer = customer + 1
        a = a + 1
    else :
        print("[ ]" + str(customer) +'번째 손님 (소요시간 : ' + str(time) + '분)')
        customer = customer + 1
print(str(a) + '명 태웠습니다.' )
