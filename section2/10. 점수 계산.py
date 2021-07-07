n = int(input())
answer = list(map(int, input().split()))
score = 0
extra = 0

for x in answer:
    if x == 1:
        extra += 1
        score += extra
    else:
        extra = 0

print(score)
