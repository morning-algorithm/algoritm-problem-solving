import sys
#sys.stdin = open("input.txt","rt")

#me
'''로직은 맞음.
!오타 실수 주의!!!
res 에 저장하기!!
또, cnt는 1부터 시작한다는 것 유의!! 
n,m = map(int,input().split())
a = list(map(int,input().split()))

def get_cnt(x):
    sum = 0
    cnt = 1
    for item in a:
        #여기에 잘못된 코드가 있었음
        if sum + item <= x:
            sum += item
        else:
            cnt+=1
            sum = item
    return cnt

s = 1
e= sum(a)
res = 0

while s<=e:
    mid = (s+e)//2
    if m >= get_cnt(mid): #cnt가 더 작은 것은 답이 될 수 있다.
        res = mid
        e = mid-1
        
    else:
       s = mid+1

print(res)
'''

#answer
'''
DVD한장의 최소치: 1, 최대치: 모든 용량을 더한 45
중간값인 22로 하면 DVD 두장에 담을 수 있음 => 최대 3장이니까 답이 될 수 있음. 일단 답으로 저장
이제 범위를 좁혀나가야한다.
'''

def Count(capacity):
    cnt=1
    sum=0
    for x in Music:
        if sum+x>capacity:
            cnt+=1
            sum=x
        else:
            sum+=x
    return cnt

n, m=map(int, input().split())
Music=list(map(int, input().split()))
lt=1
rt=sum(Music)
res=0

# 반례: 
조건이 하나 더 추가되어야함. 디비디의 최소 용량은  어떤 노래보다도 크거나 같아야함.
maxx = max(Music)

while lt<=rt:
    mid=(lt+rt)//2
    if mid>=maxx and Count(mid)<=m:
        res=mid
        rt=mid-1
    else:
        lt=mid+1
print(res)
