# 최대공약수와 최소공배수를 구하는 문제
# 최소공배수를 구하는 과정에서 비효율이 발생한 것으로 보임.

import sys
input = sys.stdin.readline

a, b = map(int, input().split())

for i in range(min(a, b), 0, -1) :
    if a % i == 0 and b % i == 0 :
        greatest_common = i
        break

least_common = int(a * b / greatest_common)

print(greatest_common)
print(least_common)

# 시간초과