import sys
sys.stdin = open("input.txt","rt")

#me
'''out of index error
def rotate(row, dir, num):
    a = aa[row - 1]
    b = [0]*n
    for i in range(n):
        if dir == 0:
            if num > i:
                b[i+ (num-1)] = a[i]
            else:
                b[i - num] = a[i]
        else:
            if num > i:
                b[i+ (num +1)] = a[i]
            else:
                b[i - num] = a[i]
    aa[row - 1] = b

n = int(input())
aa = [list(map(int,input().split())) for _ in range(n)]

m = int(input())
for _ in range(m):
    row, dir, num = map(int,input().split())
    rotate(row, dir, num)
'''

#answer
''' pop, append/insert 이용! 
pop을 하면 자동으로 땡겨진다 '''
n = int(input())
aa = [list(map(int,input().split())) for _ in range(n)]

m = int(input())
for _ in range(m):
    row, dir, num = map(int,input().split())
    if dir == 0 :
        for _ in range(num):
            aa[row-1].append(aa[row-1].pop(0))
    else:
        for _ in range(num):
            aa[row-1].insert(0,aa[row-1].pop())
    

res=0
s=0
e=n-1
for i in range(n):
    for j in range(s, e+1):
        res+=aa[i][j]
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1
print(res)
