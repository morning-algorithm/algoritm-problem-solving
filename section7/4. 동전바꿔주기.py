import sys
#sys.stdin = open("input.txt","rt")

#me
'''
def dfs(L,s,sum):
    print(L)
    global res

    
    if sum > T:
        return
    
    if L == cnt:
        print(b)
        if sum == T:
            res += 1
            print(b)
        return

    for i in range(s,cnt):
        b.append(a[L])
        dfs(L+1, i+1, sum+a[i])
        b.pop()
    
a = []
b = []
T = int(input())
k = int(input())
cnt = 0
res = 0
for _ in range(k):
    p, n = map(int,input().split())
    a.extend([p]*n)
    cnt += n

dfs(0,0,0)

print(a)
print(cnt)
print(res)
'''

#answer
'''조합, 순열 등의 개념이 아니엇음
상태트리를 잘 구성하는 것이 관건이었음
이번에는 상태트리의 각 가지가 각 원소의 사용 횟수를 나타내도록 구성

각 레벨의 노드: 이전까지의 sum값
각 가지: 각 레벨에 해당하는 원소의 사용 횟수
레벨 0 노드:              0
레벨 0 가지:    0      1      2     3  (레벨 0에 해당하는 원소의 사용횟수를 결정한다)
레벨 1 노드:    0      5      10    15
레벨 1 가지: 0  1  2
레벨 2 노드: 0  10 20 
'''

def dfs(L,sum):
    global cnt
    
    if sum > T:
        return
    
    if L == k:
        if sum == T:
            cnt += 1
        return

    for i in range(0,b[L]+1):
        dfs(L+1, sum + a[L]*i)
        
a = []
b = []
cnt = 0
T = int(input())
k = int(input())
for _ in range(k):
    p, n = map(int,input().split())
    a.append(p)
    b.append(n)

dfs(0,0)
print(cnt)
