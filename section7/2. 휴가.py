import sys
#sys.stdin=open("input.txt", "r")

def DFS(idx, total):
    global max
    
    if idx == n:
        if total > max:
            max = total
    else:
        if idx+days[idx] <= n:
            DFS(idx+days[idx], total+price[idx])
        DFS(idx+1, total)
        

n = int(input())
days = list()
price = list()
max = 0

for i in range(n):
    d, p = map(int, input().split())
    days.append(d)
    price.append(p)

DFS(0, 0)
print(max)
