import sys
#sys.stdin=open("input.txt", "rt")

T=int(input())
m=[]
for i in range(T):
    a=list(map(int, input().split()))
    if a[0]==a[1] and a[1]==a[2]:
        m.append(10000+a[0]*1000)
    elif a[0]==a[1] or a[2]==a[0]:
        m.append(1000+100*a[0])
    elif a[1]==a[2]:
        m.append(1000+100*a[1])
    else:
        m.append(100*max(a))
m.sort()
print(m[T-1])
