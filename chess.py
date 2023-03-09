import sys
input = sys.stdin.readline

ideal_w = [['w', 'b', 'w', 'b', 'w', 'b', 'w', 'b'], ['b', 'w', 'b', 'w', 'b', 'w', 'b', 'w'], 
['w', 'b', 'w', 'b', 'w', 'b', 'w', 'b'], ['b', 'w', 'b', 'w', 'b', 'w', 'b', 'w'], 
['w', 'b', 'w', 'b', 'w', 'b', 'w', 'b'], ['b', 'w', 'b', 'w', 'b', 'w', 'b', 'w'], 
['w', 'b', 'w', 'b', 'w', 'b', 'w', 'b'], ['b', 'w', 'b', 'w', 'b', 'w', 'b', 'w']]

ideal_b = [['b', 'w', 'b', 'w', 'b', 'w', 'b', 'w'], ['w', 'b', 'w', 'b', 'w', 'b', 'w', 'b'], 
['b', 'w', 'b', 'w', 'b', 'w', 'b', 'w'], ['w', 'b', 'w', 'b', 'w', 'b', 'w', 'b'], 
['b', 'w', 'b', 'w', 'b', 'w', 'b', 'w'], ['w', 'b', 'w', 'b', 'w', 'b', 'w', 'b'], 
['b', 'w', 'b', 'w', 'b', 'w', 'b', 'w'], ['w', 'b', 'w', 'b', 'w', 'b', 'w', 'b']]

board = list()
paint_w = list()
paint_b = list()
y, x = map(int, input().split())



for i in range(y - 7) :
    count = 0
    for j in range(x - 7) :
        if 