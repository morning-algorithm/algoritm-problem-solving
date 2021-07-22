import sys
#sys.stdin=open("input.txt", "r")

def DFS(x):
    if x == n+1:
        for i in range(1, n+1):
            if use[i] == 1:
                print(i, end=' ')
        print()
    else:
        use[x] = 1 #숫자 사용
        DFS(x+1)

        use[x] = 0 #숫자 사용X
        DFS(x+1)

n = int(input())
use = [0]*(n+1)

DFS(1)

