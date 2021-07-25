import sys
#sys.stdin=open("input.txt", "r")

def RecurNum(x):
    global count
    if x == m:
        count += 1
        for j in range(m):
            print(select[j], end=" ")
        print()
    else :
        for i in range(1, n+1):
            if use[i] == 0:
                select[x] = i
                use[i] = 1
                RecurNum(x+1)
                #use[i] = 0

n, m = map(int, input().split())
use = [0]*(n+1)
select = [0]*m
count = 0

RecurNum(0)

print(count)
