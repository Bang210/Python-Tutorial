# 각각의 길이가 주어지는 N그루의 나무에 대해, 한 번에 h만큼의 높이에서 잘랐을 때 M만큼의 나무를 얻기 위한 h의 최댓값을 구하는 문제

import sys
input = sys.stdin.readline

num_trees, required = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort(reverse=True)
trees_set = list(set(trees))
trees_set.sort(reverse=True)
trees_dic = dict()
h = trees[0]
cut = 0

for tree in trees_set :
    trees_dic[tree] = 0

for tree in trees :
    trees_dic[tree] += 1

while cut < required :
    cut = 0
    h -= 1
    for tree in trees_set :
        if tree > h :
            cut += (tree - h) * trees_dic[tree]
        else :
            break

print(h)

# 시간초과.