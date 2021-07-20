import sys
import heapq as hq
#sys.stdin=open("input.txt","r")

a=[]

while True:
    n=int(input())
    if n==-1:
        break
    if n==0:
        if len(a)==0:
            print(-1)
        else:
            print(hq.heappop(a)) # 힙 a의 루트 노드를 pop (맨 마지막 원소를 루트에. down heap으로 재배치)
    else:
        hq.heappush(a,n) # 힙 a에 숫자 n을 push (up heap)