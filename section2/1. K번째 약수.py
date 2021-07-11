import sys
#sys.stdin= open("input.txt","rt")

n, k=map(int,input().split())
a=[]

for i in range(1,n+1):
    if n%i==0:
        a.append(i)
    if i==n and k-1<len(a):
        print(a[k-1])
        break
else: print(-1)

