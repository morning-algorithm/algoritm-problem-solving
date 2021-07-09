import sys
#sys.stdin=open("input.txt", "r")

nList = [list()] * 7

for i in range(len(nList)):
    nList[i] = list(input().split())

count = 0
for i in range(3):
    for j in range(len(nList)):
        nStr = nList[j][i:i+5]
        if nStr == nStr[::-1]:
            count += 1

    kStr = ""
    for k in range(i, i+5):
        kStr += nList[k][i]

    if kStr == kStr[::-1]:
        count += 1

print(count)        
        

