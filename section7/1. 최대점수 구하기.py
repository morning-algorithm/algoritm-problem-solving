import sys
#sys.stdin=open("input.txt", "r")

def DFS(idx, tSum, total):
    global max
    if idx == n:
        if total > max and tSum <= m:
            max = total
    else:
        DFS(idx+1, tSum + time[idx], total + score[idx])
        DFS(idx+1, tSum, total)


n, m = map(int, input().split())

time = list()
score = list()
max = 0

for i in range(n):
    s, t = map(int, input().split())
    time.append(t)
    score.append(s)


DFS(0, 0, 0)
print(max)
