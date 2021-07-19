import sys
from collections import deque
#sys.stdin = open("input.txt","rt")

#me
'''정렬이용'''
n = int(input())
a = deque(sorted([input() for _ in range(n)]))
b = deque(sorted([input() for _ in range(n-1)]))

while b:
    ap = a.pop()
    bp = b.pop()
    if ap != bp:
        print(ap)
        break
else:
    print(a.pop()) #중간에 break되지 않으면 무조건 마지막 단어가 없는 단어

#answer
'''
딕셔너리이용.
키=1 으로 세팅하고, 그 후에 들어오는 단어들은 키=0으로 세팅해서 최종적으로 키가 1인것이 답'''