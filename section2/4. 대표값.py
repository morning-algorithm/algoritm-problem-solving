n = int(input())
score = list(map(int, input().split()))
difference = [0]*n

#half 지점에서 짝수 쪽으로 간다 => 4.5->4, 5.5->6
#따라서 rount 사용하지 말고 +0.5를 해주도록
#average = round(sum(score)/n) 
average = int(sum(score)/n + 0.5)

#나의 코드
'''for i in range(n):
    difference[i] = abs(score[i] - average)

minDif = min(difference)

minIndex = 0
for i in range(n):
    if (abs(score[i] - average) == minDif) and (score[i] > score[minIndex]):
        minIndex = i
        
print(average, minIndex+1)'''

#정답 코드 
minDif = 2147000000
minIndex = 0
for idx, x in enumerate(score):
    currentDif = abs(x-average)
    if currentDif < minDif:
        minDif = currentDif
        minIndex = idx
    elif currentDif == minDif:
        if x > score[minIndex]:
            minIndex = idx

print(average, minIndex+1)
