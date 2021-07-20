
import sys
import heapq as hq
#sys.stdin = open("input.txt","rt")

#me
'''hint (-n, n) 이용하면 최소힙 이용해서 최대힙 구현 가능! 
n이 커지면 -n은 작아짐. 제일 큰n이 제일 최소값이된다.'''

a=[]
while True:
    n = int(input())

    if n == - 1:
        break
    elif n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(hq.heappop(a)[1])
    else:
        hq.heappush(a,(-n,n))

