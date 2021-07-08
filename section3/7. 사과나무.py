import sys
#sys.stdin = open("input.txt","rt")

#me
n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]

m = n//2 #배열은 0부터 시작하므로 +1할 필요 없음
s = 0
for i in range(m+1):
    s += sum(a[i][m-i:m+i+1])

for i in range(m+1,n):
    s += sum(a[i][m-(n-1-i):m+(n-1-i)+1])
print(s)

#answer
'''2로 나눈 몫과 start,end를 사용
res=0
s=e=n//2
for i in range(n):
    for j in range(s, e+1):
        res+=a[i][j]
    if i<n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1
print(res)
'''

