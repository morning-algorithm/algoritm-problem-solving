'''my code
num = list(range(1, 21))

for i in range(10):
    a, b = map(int, input().split())

    for j in range(a-1, (a+b)//2):
        x = j
        y = (a+b-2) - j
        num[x], num[y] = num[y], num[x] #swap
'''
#answer
num = list(range(21))
for i in range(10):
    a, b = map(int, input().split())

    for j in range((b-a+1)//2):
        num[a+j], num[b-j] = num[b-j], num[a+j]

num.pop(0)
for x in num:
    print(x, end=' ')
