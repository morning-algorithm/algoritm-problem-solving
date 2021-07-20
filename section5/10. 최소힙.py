
import sys
#sys.stdin = open("input.txt","rt")

#me
a = [-1]

while True:
    n = int(input())
    if n==-1:
        break
    elif n == 0:
        if len(a) == 1: #이진트리 배열 idx는 1부터 시작하기 때문 
            print(-1)
            break
        else:
            print(a[1])
            if len(a) > 2 :
                key = a[1] = a.pop() #루트노드에 마지막 요소 일단 넣기
                me = 1
                while (len(a)-1 >= me * 2 and key > a[me * 2]) or (len(a)-1 >= me * 2 + 1 and key > a[me * 2 + 1]):
                    if len(a)-1 >= me * 2 + 1:
                        if a[me * 2] < a[me * 2 + 1]:
                            a[me] = a[me * 2]
                            me = me * 2
                        else:
                            a[me] = a[me * 2 + 1]
                            me = me * 2 + 1
                    else:
                        a[me * 2] = a[me]
                        me = me * 2
                    a[me] = key
    else:
        a.append(n)
        key = n
        me = len(a) - 1
        if len(a) != 1:
            while (me // 2) > 0 and key < a[me // 2]:
                a[me] = a[me // 2]
                me //= 2
            a[me] = key
            


#answer
'''
import heapq #최소힙 모듈
heapq.heappush()
heapq.heappop()
'''
