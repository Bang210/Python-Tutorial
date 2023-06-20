# 컴퓨터의 수와 네트워크 연결 관계가 주어졌을 때, 1번 컴퓨터(감염됨)을 통해 바이러스에 감염되는 컴퓨터의 수를 구하는 문제

import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

num_coms = int(input())
num_connections = int(input())

coms = [0 for _ in range(num_coms + 1)]
visit = [0 for i in range(num_coms + 1)]
graph = [[0] * (num_coms + 1) for j in range(num_coms + 1)]

for k in range(num_connections) :
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def virus(start) :
    coms[start] = 1
    visit[start] = 1
    for l in range(1, num_coms + 1) :
        if visit[l] == 0 and graph[start][l] == 1 :
            virus(l)

virus(1)
print(coms.count(1) - 1)


# dfs를 통해 해결
# 정답