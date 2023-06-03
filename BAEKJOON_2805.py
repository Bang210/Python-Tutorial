# 각각의 길이가 주어지는 N그루의 나무에 대해, 한 번에 h만큼의 높이에서 잘랐을 때 M만큼의 나무를 얻기 위한 h의 최댓값을 구하는 문제
# 완전탐색 방법으로 실패하고 딕셔너리를 이용해 시간복잡도를 줄여보려 했으나 실패
# 이분탐색을 이용해 재도전

import sys
input = sys.stdin.readline

num_trees, required = map(int, input().split())
trees = list(map(int, input().split()))
start = 0
end = max(trees)

while start <= end :
    h = (start + end) // 2
    cut = 0
    for tree in trees :
        if tree > h :
            cut += tree - h
    if cut < required :
        end = h - 1
    elif cut >= required :
        start = h + 1

print(end)

# 정답