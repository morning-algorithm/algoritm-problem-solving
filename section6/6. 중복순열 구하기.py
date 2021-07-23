import sys
#sys.stdin=open("input.txt", "r")

#이거 DFS인가,,대충 비슷해보이긴 하는데 재귀만 해당이 아닌가,,흠
def RecurNum(x): 
    global count
    if x == m:
        count += 1
        for j in range(m):
            print(select[j], end=" ")
        print()
    else :
        for i in range(1, n+1):
            select[x] = i
            RecurNum(x+1)

n, m = map(int, input().split())
select = [0]*m
count = 0

RecurNum(0)

print(count)
