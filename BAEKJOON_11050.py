# 주어진 N과 K에 대해 이항계수 (N)를 구하는 문제
#                            (K)

import sys
input = sys.stdin.readline

def fact(num) :
    if num < 1 :
        return 1
    elif num == 1 :
        return 1
    else :
        a = 1
        while num > 1 :
            a *= num
            num -= 1
        return a

n, k = map(int, input().split())
ans = fact(n) // (fact(n - k) * fact(k))

print(ans)

# 이항계수에 대해서도 공부해야 하나...?
# 정답