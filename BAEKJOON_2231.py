#가장 작은 분해합(ex. 256 == 245 + 2 + 4 + 5)을 구하는 문제

import sys
input = sys.stdin.readline

num = int(input())

if num - 9 * len(str(num)) > 0 :
    startingNumber = num - 9 * len(str(num))
else :
    startingNumber = 0

for i in range(startingNumber, num) :
    test = i + sum(map(int, str(i)))
    if test == num :
        creator = i
        break
    else :
        creator = 0

print(creator)

# 시간복잡도의 최소화를 위해 startingNumber을 이용했으나, 이로 인해 i가 음수가 되면서 형변환 과정에서 Value Error가 발생했던 것으로 보임.
# 따라서 startingNumber을 음이 아닌 정수로 고정한 후 시도해 해결됨.

# 정답.