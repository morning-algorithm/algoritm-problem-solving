n = int(input())

meeting = []
for i in range(n):
    start, end = map(int, input().split())
    meeting.append((start, end)) #튜플 자료로 리스트에 추가

meeting.sort(key=lambda x : (x[1], x[0])) #정렬 우선순위가 x[1] 번이 첫 순위, x[0] 번이 두 번째 순위

endTime = 0
result = 0

for start, end in meeting:
    if start >= endTime:
        endTime = end
        result += 1

print(result)
