import sys
#sys.stdin=open("input.txt", "rt")

cnt=0
a=[0]*5
arr=[]

for i in range(7):
    arr.append([])
    arr[i]=list(map(int, input().split()))

for i in range(7):
    for j in range(3):
        a=arr[i][j:j+5]
        if a[0]==a[4] and a[1]==a[3]:
            cnt+=1
        a=[arr[j][i],arr[j+1][i],arr[j+2][i],arr[j+3][i],arr[j+4][i]]
        if a[0]==a[4] and a[1]==a[3]:
            cnt+=1

print(cnt)