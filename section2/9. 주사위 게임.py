n = int(input())

maxMoney = 0

for i in range(n):
    tmp = input().split()
    tmp.sort()
    a, b, c = map(int, tmp)
    if a==b and b==c: #3개 일치
        money = 10000 + (a*1000)
    elif a==b or a==c: #a와 다른 숫자 2개 일치
        money = 1000 + (a*100)
    elif b==c: #b와 c 2개 일치
        money = 1000 + (b*100)
    else:
        money = 1000 + (b*100)

    if maxMoney < money:
        maxMoney = money

print(maxMoney)
