n,m = map(int, input().split())
dy = [0]*(m+1)
for i in range(n):
  ps, pt = map(int, input().split()) # pt:푸는데 걸리는 시간, ps:풀면 얻는 점수
  for j in range(m, pt-1, -1): # 최대시간부터 푸는데걸리는 시간까지 역순으로 계산하면 2차원 배열을 사용하지 않아도 됨.
    dy[j] = max(dy[j], dy[j-pt]+ps)
print(dy[m])
