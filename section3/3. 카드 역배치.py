import sys
#sys.stdin=open("input.txt", "r")

num = list(range(0,21))
for i in range(10):
    s, e=map(int, input().split())
    for j in range((e-s+1)//2):
        num[s+j], num[e-j]=num[e-j], num[s+j]

num.pop(0)
for i in range(len(num)):
    print(num[i], end=' ')
