#가장 작은 분해합(ex. 256 == 245 + 2 + 4 + 5)을 구하는 문제

import sys
input = sys.stdin.readline

num = int(input())
startingNumber = num - 9 * len(str(num))

for i in range(startingNumber, num) :
    test = i
    for j in range(len(str(i))) :
        test += int(str(i)[j])
    if test == num :
        creator = i
        break
    else :
        creator = 0

print(creator)

# 정답.