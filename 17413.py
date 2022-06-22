from collections import deque
import sys

input = sys.stdin.readline

s = input().rstrip()

word = ''
tag = False
result = ''

for i in s:
    if tag == False:
        if i == '<':
            tag = True
            word = word + i
        elif i == ' ':  #공백이면 단어를 구분지음 --> 공백일때 result에 넣어주기
            word = word + i
            result = result + word
            word = ''
        else:
            word = i + word     #뒤집어서 출력위해

    else:
        word = word + i
        if i == '>':
            tag = False
            result = result + word
            word = ''

print(result+word)