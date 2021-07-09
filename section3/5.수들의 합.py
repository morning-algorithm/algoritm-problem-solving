
import sys
sys.stdin = open("input.txt","rt")

#me 
'''time limit 통과 실패 
N, M = map(int,input().split())
l = list(map(int,input().split()))

cnt = 0
for i in range(N):
    for j in range(i,N):
        s = sum(l[i:j+1])
        if s == M:
            cnt+=1
        if s >= M:
            break
print(cnt)
'''

#answer
'''lt,rt를 써서 lt~rt-1까지의 값을 total로보고 rt,lt범위를 조정함'''

N, M = map(int,input().split())
a = list(map(int,input().split()))
lt = 0
rt = 1
tot = a[0]
cnt = 0

while True:
    if tot < m:
        if rt < n :
            tot += a[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= a[lt]
        lt+=1
    elif tot > m:
        tot-=a[lt]
        lt+=1
print(cnt)
