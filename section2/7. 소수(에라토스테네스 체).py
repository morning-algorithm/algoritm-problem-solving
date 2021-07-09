import sys
#sys.stdin=open("input.txt", "rt")

n = int(input())
countList = [0]*(n+1)
count = 0

for i in range(2, n+1):

    if countList[i] == 0:
        count += 1

        for j in range(i, n+1, i):
            countList[j] = 1


print(count)
