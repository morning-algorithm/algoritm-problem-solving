import sys
#sys.stdin=open("input.txt", "r")

def DFS(x, sum):
    global max

    if sum > c:
        return
    
    if x == n:
        if sum <= c and sum > max:
            max = sum
    else:
        use[x] = 1 #숫자 사용
        DFS(x+1, sum + w[x])

        use[x] = 0 #숫자 사용X
        DFS(x+1, sum)

max = 0       
c, n = map(int, input().split())
use = [0]*n
w = []

for i in range(n):
    w.append(int(input()))

DFS(0, 0)
print(max)

'''
wSum = 0;
w.sort(reverse = True)
for i in range(n):
    if (wSum + w[i]) < c:
        wSum += w[i]

print(wSum)

'''
