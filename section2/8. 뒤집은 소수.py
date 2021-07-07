def reverse(x):
    s = str(x)
    n = ""
    for i in range(len(s)-1, -1, -1):
        n += s[i]
        
    return int(n)

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x//2+1):
        if x%i == 0:
            return False
    else:
        return True
    
n = int(input())
num = list(map(int, input().split()))
for x in num:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')
