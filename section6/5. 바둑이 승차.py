import sys
#sys.stdin = open("input.txt","rt")

#me
''' 함수 호출전에 조건 먼저 검사! 들어가서 검사했을 땐 time limit발생'''
def dfs(i,s):
      global m

      '''
      if s > c :
            return
      '''
      
      if i == n: #마지막 원소 초과. 끝까지 왔음. 합을 비교
            if m < s :
                  m = s
      else:
            if s+a[i] < c: #함수 호출전에 조건 먼저 검사! 이거 안하고 들어가서 검사했을 땐 time limit발생.
                  dfs(i+1, s+a[i]) #원소 사용
            dfs(i+1, s) #원소 사용 안함
            
c,n = map(int,input().split())
a = [ int(input()) for _ in range(n)]
global m 
m = -1
dfs(0,0)
print(m)


#answer
'''
해당 바둑이를 넣을까 안넣을까. 부분집합을 만들어보고. 부분집합의 합이 c를 넘지 않으면 max갱신
sum>c를 넘어가는 것을 커트하는 것 이상으로 더 가지수를 줄여줘야함.
그 방법: 
tsum은 상태에 상관없이 자신을 더한 값.
(total - tsum)은 앞으로 판단해야할 바둑이들의 총 무게
sum + (total - tsum) < max : # 만약 앞으로 남은 놈들까지 다 더했는데 max보다 작다면? 더이상 더 들어가볼 가치가 없다.
      return
'''
