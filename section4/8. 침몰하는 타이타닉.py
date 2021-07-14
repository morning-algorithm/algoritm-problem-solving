import sys
#sys.stdin=open("input.txt", "r")

n, m = map(int, input().split())
nList = list(map(int, input().split()))

boat = 0
sum = 0
count = 0

e = n-1
i = 0

while i <= e:
    weight = nList[i]
    count += 1
    boat += 1

    for j in range(e, 0, -1):
        if (weight + nList[j]) <= m:
            count += 1
            e -= 1
            i += 1
            break;
        
print(boat)



''' #처음 코드 (보트 당 사람 2명 고려X)
for i in range(n):
    weight = sum + nList[i]
    if weight <= m and count < 2:
        sum += nList[i]
        count += 1
    elif weight > m or count > 2:
        boat += 1
        sum = nList[i]
        count = 0
'''


