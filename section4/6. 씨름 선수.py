n = int(input())

player = []

for i in range(n):
    height, weight = map(int, input().split())
    player.append((height, weight)) #튜플 자료로 리스트에 추가

result = 0

'''my code
for i in range(n):
    isMax = True
    for j in range(n):
        if i != j:
            if player[i][0] < player[j][0] and player[i][1] < player[j][1]:
                isMax = False
    if isMax:
        result += 1
'''

player.sort(reverse=True)
largest = 0
result = 0

#키는 이미 정렬되어 있으니, 몸무게만 비교
for h, w in player:
    if w > largest:
        largest = w
        result += 1
        
print(result)
