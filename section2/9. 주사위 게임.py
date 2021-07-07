import sys
#sys.stdin=open("input.txt", "rt")

n = int(input())
maxM = 0

for i in range(n):
    pList = list(map(int, input().split()))
    
    if pList[0] == pList[1] and pList[1] == pList[2]:
        m = 10000+(pList[0]*1000)

    elif pList[0] == pList[1] or pList[0] == pList[2]:
        m = 1000+(pList[0]*100)

    elif pList[1] == pList[2]:
        m = 1000+(pList[1]*100)

    else:
        m = max(pList)*100

    if(m > maxM):
        maxM = m


print(maxM)
