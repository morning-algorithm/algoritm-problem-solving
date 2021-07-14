import sys
#sys.stdin=open("input.txt", "r")

n = int(input())
nList = list(map(int, input().split()))

strList = []
count = 0

e = n-1
s = 0
before = 0

while s <= e:

    if (nList[s] > before) and (nList[e] > before): #둘 다 before보다 큰 경우
        count += 1
        if nList[s] < nList[e]:
            strList.append("L")
            before = nList[s]
            s += 1
        elif nList[e] < nList[s]:
            strList.append("R")
            before = nList[e]
            e -= 1
    elif (nList[s] > before) or (nList[e] > before): #하나만 before보다 큰 경우
        count += 1
        if nList[s] > before:
            strList.append("L")
            before = nList[s]
            s += 1
        elif nList[e] > before:
            strList.append("R")
            before = nList[e]
            e -= 1
    else: break;
            
print(count)
print("".join(strList))

