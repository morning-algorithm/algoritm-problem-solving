import sys
import heapq
#sys.stdin=open("input.txt", "r")

heap = []

while True:
    n = int(input())

    if n == 0:
        if len(heap) != 0:
            print(heapq.heappop(heap))
        else:
            print(-1)
    elif n == -1:
        break;
    else:
        heapq.heappush(heap, n)

    
        
