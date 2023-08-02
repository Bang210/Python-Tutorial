import sys
import heapq
input = sys.stdin.readline

num = int(input())
heap = []

for i in range(num) :
    com = int(input())
    if com == 0 :
        if len(heap) == 0 :
            print(0)
        else :
            print(heapq.heappop(heap) * (-1))
    else :
        heapq.heappush(heap, com * (-1))