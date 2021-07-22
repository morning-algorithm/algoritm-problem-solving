import sys
#sys.stdin=open("input.txt", "r")

c, n = map(int, input().split())
w = []

for i in range(n):
    w.append(int(input()))

'''
wSum = 0;
w.sort(reverse = True)
for i in range(n):
    if (wSum + w[i]) < c:
        wSum += w[i]

print(wSum)

'' 
