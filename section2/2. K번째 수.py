import sys
#sys.stdin=open("input.txt", "rt")

T=int(input())

for i in range(0, T):
    n, s, e, k = map(int, input().split())
    num=list(map(int, input().split()))
    num=num[s-1:e]
    num.sort()
    print("#%d %d" %(i+1, num[k-1]))    
