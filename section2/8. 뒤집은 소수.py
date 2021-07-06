import sys
#sys.stdin=open("input.txt", "rt")

n = int(input())
numList = list(input().split())
reNumList = [0]*(n+1)

def reverse(x):
    n = int(x[::-1])
    return n

def isPrime(x):

    if x == 1:
        return False
    
    for i in range(2, x):
        if x%i == 0:
            return False
    else:
        return True

for i in range(n):
    reNumList[i] = reverse(numList[i])

    if isPrime(reNumList[i]):
        print(reNumList[i], end=" ")
