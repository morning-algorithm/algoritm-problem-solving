import sys
#sys.stdin = open("input.txt", "rt")

T = int(input())

for t in range(T):
    N,s,e,k = map(int, input().split())
    l = list(map(int,input().split()))
    sl = sorted(l[s-1:e])
    print(f'#{t+1} {sl[k-1]}')


