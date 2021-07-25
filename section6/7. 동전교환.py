import sys
#sys.stdin=open("input.txt", "r")

def RecurNum(sum):
    #print(sum)
    global count
    if sum == m:
        print(count)
        sys.exit(0)
    
    for j in range(n):
       if (sum + coin[j]) <= m:
           sum += coin[j]
           count += 1
           RecurNum(sum)

n = int(input()) 
coin = list(map(int, input().split()))
coin.sort(reverse=True)
m = int(input()) 
count = 0

RecurNum(0)

