def solution(n,l,m):
  dy = [1000]*(m+1) # 동전개수는 무한이지만 최대 거스름돈이 500원이므로 최대 동전개수는 500이하
  dy[0] = 0 # 이 부분이 중요 !
  for i in range(n):
    w = l[i]
    for j in range(w,m+1):
      dy[j] = min(dy[j], dy[j-w] + 1) # min임이 중요!
  return dy[m]
