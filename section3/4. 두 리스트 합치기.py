import sys
#sys.stdin=open("input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

#n
i=0
j=0
c=[]
while True:
    if a[i]<b[j]:
        c.append(a[i])
        i+=1
    elif a[i]==b[j]:
        c.append(a[i])
        c.append(b[j])
        i+=1
        j+=1
    else:
        c.append(b[j])
        j+=1
    if i==n:
        c=c+b[j:]
        break
    elif j==m:
        c=c+a[i:]
        break

for x in c:
   print(x, end=' ')

#nlogn

#n=n+m
#n.sort()
#for x in n:
#   print(x, end=' ')
#