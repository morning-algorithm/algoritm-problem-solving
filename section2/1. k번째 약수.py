N, K = map(int, input().split()) #띄어쓰기 기준으로 split
cnt = 1 #약수 1 은 이미 포함
for x in range(2,N+1):
    if N % x == 0:
        cnt += 1
    if cnt == K:
        print(x)
        break
else: #for문이 정상적으로 끝나면 else 를 한다
    print(-1)
