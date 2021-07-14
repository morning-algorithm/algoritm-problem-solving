import sys
#sys.stdin=open("input.txt", "r")

n = int(input())
nList = list(map(int, input().split()))
num  = [0]*n

for i in range(n):
    for j in range(n):
        if nList[i] == 0 and num[j] == 0:
            num[j] = i+1
            break;
        elif num[j] == 0:
            nList[i] -= 1

#print(num)
for x in num:
    print(x, end=" ")
