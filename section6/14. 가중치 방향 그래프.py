import sys
sys.stdin=open("input.txt", "r")
# 인접 행렬 (가중치 방향 그래프)
n,k= map(int, input().split())
arr=[[0]*n for _ in range(n)]

for i in range(k):
    a,b,c=map(int, input().split())
    arr[a-1][b-1]=c

for i in range(n):
    print(arr[i])