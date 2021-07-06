import sys
#sys.stdin= open("input.txt","rt")

n, m=map(int,input().split())# 4, 6, 7, 12, 20
a=[]

for i in range(1, n+1):
    for j in range(1, m+1):
        a.append(i+j);

s = set(a)

cnt = []

s=list(s)
for x in s:
    cnt.append(a.count(x))

max_cnt=max(cnt)

for i in range(len(cnt)):
    if cnt[i]==max_cnt:
        print(s[i],end=" ")


