import sys
sys.stdin = open("input.txt","rt")


#me
'''
이해가 안가는점:
마지막에 가지수가 엄청나게 나올텐데 어떻게 가지를 치지 않고 이렇게 빨리 나오지?
사람이 3명이고 동전에 12개면 마지막 리프노드는 총 3^12 = 531441 인데 이게 맞는건가..?
'''
def dfs(L,s1,s2,s3):
    global m
    if L == n:
        if s1 != s2 and s2 != s3 and s1 != s3:
            tmp = max(s1,s2,s3) - min(s1,s2,s3)
            if m > tmp:
                m = tmp
        return

    dfs(L+1, s1 + a[L], s2, s3)
    dfs(L+1, s1 , s2 + a[L] , s3)
    dfs(L+1, s1 , s2  , s3 + a[L])

    
n = int(input())
a = [ int(input()) for _ in range(n) ]
m = 9999999
dfs(0,0,0,0)

print(m)

#answer
'''
dfs문제같다 => 바로 상태트리를 그리려고 해야함
각 레벨마다 각 사람의 누적합을 더하는 money = [0]*3 배열을 만들고
for문해서 들어갈 때 
'''
