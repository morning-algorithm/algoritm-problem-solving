import sys
#sys.stdin=open("input.txt", "rt")

n=list(range(1,21))
m=[]
x=0
y=0
t=0
for i in range(10):
    x,y=map(int, input().split())
    t=x-1
    m=reversed(n[x-1:y])
    for a in m:
        n[t]=a
        t+=1
for i in range(20):
    print(n[i], end=" ")