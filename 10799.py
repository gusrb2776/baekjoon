s = input().rstrip()

#( ( ( ()() ) ( () ) () ) )
#       3      2
#       5
#       5
#1 2 3 r1 r2  2개 * 3                6
#             3 r1 1개*3             3
#                 2  r1  1개*2       2
#총 긴 스틱수 = 4개                    4

#stick은 ( 다음에 또 (
#laser은 ( 다음에 )
#stick은 ) 뒤에 )면 사라짐

total_stick = 0
cur_stick = 0
laser = 0
num = 0

for i in range(len(s)-1):
    if s[i] == '(' and s[i+1] == ')':
        num += cur_stick
    elif s[i] == '(' and s[i+1] == '(':
        total_stick += 1
        cur_stick += 1
    elif s[i] == ')' and s[i+1] == ')':
        cur_stick -= 1

print(num + total_stick)