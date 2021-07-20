import sys
#sys.stdin=open("input.txt", "r")
from collections import deque

obj = input()
n = int(input())

for i in range(n):
    curList = input()
    m = list(obj)

    for j in range(len(curList)):
        if curList[j] in m:
            if m[0] == curList[j]:
                m.pop(0)
            else:
                break;

    if len(m) != 0:
        print("#%d NO" %(i+1))
    else:
        print("#%d YES" %(i+1))
        
    

