import sys
# 2, 4번 input 시간 오래 걸림

def DFS(idx, s):
    global count
    if s == t:
        count += 1
        return
    
    if idx == k:
        if s == t:
            count += 1
    else:
        for i in range(0, coins[idx]+1):
            DFS(idx+1, s+(price[idx]*i))
    

t = int(input())
k = int(input())

price = list()
coins = list()
count = 0


for i in range(k):
    p, c = map(int, input().split())
    price.append(p)
    coins.append(c)

DFS(0, 0)
print(count)
