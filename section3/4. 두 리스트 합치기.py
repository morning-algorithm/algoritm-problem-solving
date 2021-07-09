
import sys
sys.stdin = open("input.txt","rt")

#me 
'''
N1 = int(input())
l1 = list(map(int,input().split()))
N2 = int(input())
l2 = list(map(int,input().split()))

l1.extend(l2)
l1.sort()

for i in l1:
    print(i,end = ' ')
'''

#answer
'''
python의 sort를 사용하면 nlogn
하지만 문제에서 리스트가 **이미 정렬** 되어있으므로 for문으로 해결하면 n 복잡도가 나오게됨
데이터가 많아지면 큰 차이가 나게 됨

풀이:
두 배열에 포인트 변수를 놓고 비교하여 작은 것을 새로운 배열에 넣는다. 
한 배열이 먼저 끝나면 나머지 배열은 슬라이스로 붙인다.
'''

'''me(retry)
N1 = int(input())
l1 = list(map(int,input().split()))
N2 = int(input())
l2 = list(map(int,input().split()))
r = [0]*(N1+N2)

p1 = 0
p2 = 0
for i in range(N1 + N2):
    if p1 == N1:
        r[i:] = l2[p2:]
        break
    elif p2 == N2:
        r[i:] = l1[p1:]
        break
    else: 
        if l1[p1] <= l2[p2]:
            r[i] = l1[p1]
            p1 +=1
        else:
            r[i] = l2[p2]
            p2 +=1
print(r)
'''

N1 = int(input())
l1 = list(map(int,input().split()))
N2 = int(input())
l2 = list(map(int,input().split()))
r = []
p1=p2=0

while p1<N1 and p2<N2:
    if l1[p1] <= l2[p2]:
        r.append(l1[p1])
        p1 +=1
    else:
        r.append(l2[p2])
        p2 +=1

if p1<N1:
    r = r+l1[p1:]
if p2<N2:
    r = r+l2[p2:]

for i in r:
    print(i,end = ' ')



