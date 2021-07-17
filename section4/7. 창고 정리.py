import sys
#sys.stdin=open("input.txt", "rt")

n = int(input())
a = list(map(int,input().split()))
k = int(input())

for i in range(k):
    x=a.index(max(a))
    y=a.index(min(a))
    a[x]=a[x]-1
    a[y]=a[y]+1
print(max(a)-min(a))