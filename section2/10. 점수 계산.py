import sys
#sys.stdin=open("input.txt", "rt")

n = int(input())
ansList = list(map(int, input().split()))

count = 0
sum = 0

for i in range(n):
    if ansList[i] == 1:
        count += 1
        sum += count
    else:
        count = 0

print(sum)
