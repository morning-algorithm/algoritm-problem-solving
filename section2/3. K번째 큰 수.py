import sys
#sys.stdin= open("input.txt","rt")

n, k=map(int,input().split())
a=list(map(int, input().split()))

sum=[]
for i in range(n):
    for j in range(i+1,n):
        for l in range(j+1,n):
            sum.append(a[i]+a[j]+a[l])
sum=(list(set(sum)))
sum.sort(reverse=True)

print(sum[k-1])