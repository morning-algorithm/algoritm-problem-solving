import sys
#sys.stdin = open("input.txt","rt")

n,m = map(int,input().split())

#me
def dfs(x):
    global cnt
    if x == m:
        print(' '.join(map(str,res)))
        cnt += 1
        return
    for i in range(1,n+1):
        res[x] = i
        dfs(x+1)


cnt = 0
res = [0]*m
dfs(0)
print(cnt)

#answer
'''동일'''
