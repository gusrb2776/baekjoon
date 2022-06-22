from collections import deque
import sys

input = sys.stdin.readline

s = input().split()
index = 0

for sentence in s:
    stack = deque()
    for i in sentence:
        if i == '<':
            index = 1
        elif i == '>':
            index = 0
        if index == 0 and i != '>':
            stack.appendleft(i)

    for j in stack:
        print(j,end='')
    print(' ',end='')