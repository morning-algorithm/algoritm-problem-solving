
import sys
#sys.stdin = open("input.txt","rt")

#me
''' 정렬만으론 절대 답이 나올 수 없음!!
n,m = map(int,input().split())
a = [int(input()) for _ in range(n)]
a.sort()
a.insert(0,0)
print(a)

b = [a[i+1]-a[i] for i in range(n)]
print(b)
b.pop(0)
b.sort()
print(b)


print(b[m-1])
'''

#answer
'''
1. 일단 정렬을 한다
2. 가장 가까운 두 말의 최소거리 lt:1 (수직선 상의 제일 앞 좌표), rt최대거리: 9(넉넉하게 수직선 상의 제일 뒤의 좌표)
3. 중간값을 구해서 그 중간값이 최대거리라고 했을때 말이 3마리 이상 배치될 수 있는지 보기 => (3마리 이상이면 답이 될 수 있다,)
    - Cnt 중간값을 최대거리로 했을 때 각 점간의 거리가 최대거리를 넘으면 말을 배치할 수 있고, 그것을 센다.
'''

def Count(x):
    p = a[0]
    cnt = 1
    for i in range(1,n):
        if a[i] - p >= x:
            cnt+=1
            p = a[i]
    return cnt

n,m = map(int,input().split())
a = [int(input()) for _ in range(n)]
a.sort()

lt = a[0]
rt = a[len(a)-1]
res = 0 
while lt<=rt:
    mid =(lt+rt) //2
    if Count(mid)>=m:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)