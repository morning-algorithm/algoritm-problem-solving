import sys
#sys.stdin=open("input.txt", "r")


def DFS(idx, sum): # idx -> level & index

    if total/2 < sum:
        return
    
    if idx == n: # 0번부터 사용해서
        if total/2 == sum:
            print("YES")
            sys.exit(0)
    else:
        DFS(idx+1, sum + nList[idx])
        DFS(idx+1, sum)  

n = int(input())
nList = list(map(int, input().split()))

total = sum(nList)
DFS(0, 0)
print("NO")

