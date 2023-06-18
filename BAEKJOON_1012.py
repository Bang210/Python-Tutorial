# 입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 
# 그 다음 줄부터 각각의 테스트 케이스에 대해 첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50), 그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다. 
# 그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다. 두 배추의 위치가 같은 경우는 없다.

# 각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력한다.

# dfs를 이용하여 해결

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

def add_search(yy, xx) :
    visit[yy][xx] = 1
    if xx < width - 1 and cabbages[yy][xx + 1] == 1 and visit[yy][xx + 1] == 0 :
        add_search(yy, xx + 1)
    if yy < length - 1 and cabbages[yy + 1][xx] == 1 and visit[yy + 1][xx] == 0 :
        add_search(yy + 1, xx)
    if xx > 0 and cabbages[yy][xx - 1] == 1 and visit[yy][xx - 1] == 0 :
        add_search(yy, xx - 1)
    if yy > 0 and cabbages[yy - 1][xx] == 1 and visit[yy - 1][xx] == 0 :
        add_search(yy - 1, xx)

num_tests = int(input())

for i in range(num_tests) :
    width, length, num = map(int, input().split())
    cabbages = [[0] * width for _ in range(length)]
    visit = [[0] * width for __ in range(length)]
    cnt = 0
    for j in range(num) :
        a, b = map(int, input().split())
        cabbages[b][a] = 1
    for y in range(length) :
        for x in range(width) :
            if (cabbages[y][x] == 1) and (visit[y][x] == 0) :
                cnt += 1
                add_search(y, x)
    print(cnt)

# 정답