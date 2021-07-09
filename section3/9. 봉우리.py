
import sys
#sys.stdin = open("input.txt","rt")

#me
def is_largest(i,j):
    num = a[i][j]
    if num <= a[i][j+1] or num <= a[i][j-1] or num <= a[i+1][j] or num <= a[i-1][j]:
        return False
    else:
        return True

n = int(input())
a = [[0]*(n+2) for _ in range(n+2)]

for i in range(1,n+1):
    a[i][1:n+1] = list(map(int,input().split()))

cnt = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if is_largest(i,j) == True:
            cnt +=1

print(cnt)

#answer
'''
tip1. 상하 좌우 탐색을
dx = [-1,0,1,0]
dy = [0,1,0,-1] 이용해서!


tip2. if or or or or 대신에 all() 함수를 사용! 모든 조건이 참일때 True

=> all(a[i+dx[k]][j+dy[k]] for k in range(4))
'''