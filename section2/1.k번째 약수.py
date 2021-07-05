import sys
#sys.stdin = open("input.txt","rt")
n, k = map(int, input().split())

''' my
l = list()
for i in range(1,n+1):
    if n % i == 0 :
        l.append(i)

if len(l) < k : 
    print(-1)
else :
    print(l[k-1])
k번째 수가 작을 수도 있는데 n의 끝까지 가고, 리스트에 넣기까지함 '''

# answer
cnt = 0
for i in range(1,n+1):
    if n % i == 0 :
        cnt += 1
    if cnt == k:
        print(i)
        break
else:  #for-else문 : break문이 걸려서 빠져나가는지 아닌지를 판단
        print(-1)


