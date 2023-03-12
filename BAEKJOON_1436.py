# '666'이 포함된, N번째로 작은 수를 구하는 문제

num = int(input())
ending = [666]
i = 1666
while len(ending) < num :
    if str(i).find('666') != -1 :
        ending.append(i)
    i += 1

print(ending[num -1])

# 정답.