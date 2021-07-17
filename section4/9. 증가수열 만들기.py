import sys
#sys.stdin=open("input.txt", "rt")

n= int(input())
a = list(map(int,input().split()))
res=[]
dir=[]

while a:
    l=len(res)
    s=len(a)
    if l>0 :
        if a[0]>res[l-1] and a[s-1]>res[l-1]:
            x=a.index(min(a[0], a[s-1]))
            res.append(a[x])
            if x==0:
                dir.append("L")
            else:
                dir.append("R")
            a.pop(x)
        elif a[0]>res[l-1]:
            res.append(a[0])
            dir.append("L")
            a.pop(0)
        elif a[s-1]>res[l-1]:
            res.append(a[s-1])
            dir.append("R")
            a.pop(s-1)
        else:
            break
    else:
        x=a.index(min(a[0], a[s-1]))
        res.append(a[x])
        if x==0:
            dir.append("L")
        else:
            dir.append("R")
        a.pop(x)

print(len(res))
for x in dir:
    print(x, end="")