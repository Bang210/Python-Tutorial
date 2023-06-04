# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 문제

import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

def fact(n) :
    if n == 1 or n == 0 :
        return 1
    else :
        return n * fact(n - 1)
    
num = int(input())

target = str(fact(num))
ans = 0
check = len(target) - 1

while True :
    if target[check] == '0' :
        ans += 1
        check -= 1
    else :
        break

print(ans)

# 정답.
# sys.setrecursionlimit()을 통해 재귀 제한을 설정