
import sys
sys.stdin = open("input.txt","rt")

#me
''' 
자꾸 어떻게 하면 최대한 for문을 안돌리고 파이썬 함수를 잘 활용해서 풀 수 있을까하다가 20분 제한시간에 걸린다.
그냥 정석대로 푸는게 나을 것 같다.

n = int(input())
l = list()
r = list()

for i in range(n):
    ll = list(map(int,input().split()))
    l.append(ll)
    r.append(sum(ll))
'''

s = 0
for i in range(n):
   
#answer
n = int(input())
a = [list(map(int,input().split())) for _ in range(n)] #2차원 리스트 한번에 읽는 방법

largest = -1
for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += a[i][j] #행 탐색
        sum2 += a[j][i] #열 탐색
    if sum1>largest:
        largest = sum1
    if sum2>largest:
        largest = sum2

sum1 = sum2 = 0
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n-i]
if sum1>largest:
    largest = sum1
if sum2>largest:
    largest = sum2

print(largest)

