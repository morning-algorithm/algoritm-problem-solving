
def DFS(st):
    if dy[st] > 0:
        return dy[st]
    if st == 1 or st == 2:
        return st
    else:
        dy[st] = DFS(st-1) + DFS(st-2)
        return dy[st]

    
n = int(input())
dy = [0] * (n+1)

print(DFS(n))
