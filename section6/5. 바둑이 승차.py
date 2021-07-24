import sys
# sys.stdin=open("input.txt", "r")

def DFS(L, sum, tsum):
    global result
    if sum+(total-tsum)<result:
        return
    if sum>c:
        return
    if L==n:
        if sum>result:
            result=sum
    else:
        DFS(L+1, sum+a[L], tsum+a[L])
        DFS(L+1, sum, tsum+a[L])


if __name__=="__main__":
    c, n=map(int, input().split())
    a=[0]*n
    result=-2147000000
    for i in range(n):
        a[i]=int(input())
    total=sum(a)
    DFS(0, 0, 0)
    print(result)


'''Time Limit Code (me)
def DFS(i):
    global max, sum
    if i == n:
        for j in range(n):
            if a[j][1]==1:
                sum+=a[j][0]
        if max<sum and sum<=m:
            max=sum
        sum=0
    else:
        a[i][1]=1 # O - 부분 집합 포함
        DFS(i+1)
        a[i][1]=0 # X - 부분 집합 제외
        DFS(i+1)


if __name__=="__main__":
    m,n= map(int,input().split())
    a=[]
    for i in range(n):
        a.append([int(input()),0])    
    max=0
    sum=0
    DFS(0)
    print(max)

'''
