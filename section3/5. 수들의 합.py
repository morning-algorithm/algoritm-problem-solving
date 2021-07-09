import sys
#sys.stdin=open("input.txt", "r")

n, m = map(int, input().split())
nList = list(map(int, input().split()))

count = 0

for i in range(n):
    sum = nList[i]
    if sum == m:
        count += 1
        break;
    for j in range(i+1, n):
        sum += nList[j]
        if sum == m:
            count += 1
        elif sum > m:
            break;

print(count)
