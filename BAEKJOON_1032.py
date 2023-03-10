# 주어진 N개의 파일에 대해, 최소한의 '?'를 사용해 어떤 검색어로 검색했는지 구하는 문제

n = int(input())
result = list()

for i in range(n) :
    result.append(input())

common = list()
for l in range(len(result[0])) :
    common.append(result[0][l])

for j in range(n-1) :
    for k in range(len(common)) :
        if common[k] == '?' :
            pass
        elif common[k] != result[j+1][k] :
            common[k] = '?'

for m in range(len(common)) :
    print(common[m], end='')

# 정답