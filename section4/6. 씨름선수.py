


#answer
''' 
지원자 입장: 나보다 키, 몸무게 둘다 큰 사람 있으면 탈락이다. 
지원자 think: 나보다 키큰사람 누구야? (작은 사람은 안중에도 없음) 그 키 큰 사람들 중에 나보다 몸무게 많은 사람 있어?

풀이: 키로 내림차 정렬 시켜놓고, 지원자 입장에서 나보다 키큰 사람 중에 몸무게 더 큰사람 있는지 검사.

여기서, 몸무게를 매번 검사하면? 이중포문
포문 한번만 돌리려면? 몸무게를 검사할때 마다 최대값을 저장하여 각 지원자는 누적된 최대값과만 비교.
'''

n = int(input())
a = [ tuple(map(int,input().split())) for _ in range(n)]
a.sort(reverse = True)

cnt = 1
max = a[0][1] #최대 몸무게
for i in range(1, n):
    if a[i][1] > max:
        max = a[i][1]
        cnt +=1

print(cnt)




