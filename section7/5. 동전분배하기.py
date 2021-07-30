def DFS(level):
    global m
    if level == n:
        if (max(money) - min(money)) < m:
            d = True
            for i in range(len(money)):
                if money.count(money[i]) > 1:
                    d = False   
            if d:
                m = max(money) - min(money)
    else:
        for i in range(person):
            money[i] += coins[level]
            DFS(level+1)
            money[i] -= coins[level]

    
n = int(input())
coins = list()

person = 3
money = [0]*person

for i in range(n):
    coins.append(int(input()))

m = sum(coins)

DFS(0)
print(m)
