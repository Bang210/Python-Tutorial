# 삼각형에서 길이를 줄일 수만 있는 세 변에 대해 최대의 둘레를 구하는 문제

len = list(map(int, input().split()))
len.sort()

if len[2] >= len[0] + len[1] :
    len[2] = len[0] + len[1] - 1

print(len[0] + len[1] + len[2])

# 정답