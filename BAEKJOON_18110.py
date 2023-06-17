# 문제 난이도에 대한 의견이 n개 주어졌을 때, 절사평균으로 계산한 최종 난이도를 출력하는 문제
# 파이썬 내부의 round함수에 대한 이해 필요

import sys
input = sys.stdin.readline

def rnd(n) :
    return int(n) + 1 if n - int(n) >= 0.5 else int(n)

num_ops = int(input())
ops = sorted([int(input()) for i in range(num_ops)])

exception = rnd(0.15 * num_ops)

ans = 0 if num_ops == 0 else rnd(sum(ops[exception:-exception] if exception else ops) / (num_ops - 2 * exception))
print(ans)

# 정답