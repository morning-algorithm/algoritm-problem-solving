import sys
#sys.stdin=open("input.txt", "rt")

n, m = map(int, input().split())

a = list(map(int, input().split()))

lt=0
rt=1
tot=a[0]
cnt=0

while True:
    if tot<m:
        if rt<n:
            tot+=a[rt]
            rt+=1
        else:
            break
    elif tot==m:
        cnt+=1
        tot-=a[lt]
        lt+=1
    else:
        tot-=a[lt]
        lt+=1
print(cnt)


#Time Limit Exceeded
#count=0

#for i in range(n):
#    if a[i]>m :
#        continue
#    for j in range(n-i):
#        if sum(a[i:i+j+1]) == m : 
#            count+=1
#            break
#print(count)