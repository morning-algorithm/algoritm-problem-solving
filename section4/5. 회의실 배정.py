import sys
#sys.stdin=open("input.txt", "rt")

n = int(input())
a=[]
cnt=1

for i in range(n):
    a.append([])
    a[i]=list(map(int, input().split()))
    
a.sort(key = lambda x : x[1])# a[][1]위치의 값을 기준으로 정렬

i=0
j=i+1
while j<n and i<n:
    if a[i][1]<=a[j][0]:
        cnt+=1
        i=j
        j=j+1
    else:
        j+=1
print(cnt)