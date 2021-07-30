import sys
sys.stdin = open("input.txt","rt")

#me
'''
부분집합 문제!
진짜 아깝게 틀림! dfs(0,0,0) 부터 시작하면 됐었음!
왜냐하면 0번째 인덱스를 아직 쓴다는 말이 아니고 쓸지 말지 결정하는 거였으니까.'''
def dfs(i,s,t):
      global max

      if t > m: #제한시간 초과시 더 볼 필요 없음
            return 
      
      if i == n : #모든 원소의 상태가 결정되면 
            if s > max: #최대점수보다 크면
                  max = s
            return
      
      dfs(i+1, s+a[i][0],t+a[i][1]) #사용
      dfs(i+1, s,t ) #사용 x

      
n,m = map(int,input().split())
a = []
max = -1

for _ in range(n):
      a.append(tuple(map(int,input().split())))

# dfs(0,a[0][0],a[0][1]) #answer: 얘는 필요없다 !!
dfs(0,0,0) 
print(max)

