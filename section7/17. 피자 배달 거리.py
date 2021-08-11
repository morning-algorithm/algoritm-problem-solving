import sys
#sys.stdin = open("input.txt","rt")

#me
'''
6개 중에 4개의 피자집 선택 => 중복이 안되고 순서 상관없으므로 중복순열x , 순열x, 조합임!

4개를 골라놓고,

4개의 피자집 중에서 각 집마다 가장 가까운 피자집을 구하면 그것이 각 집들의 피자 배달거리.
각 집의 피자 배달거리를 모두 합한 것이 도시의 피자배달거리이다.

이 도시의 피자배달거리가 최소가 나오게하는 피자집 조합을 구하면 되는 문제였다.

처음엔 부분집합+sum문제 인줄 알았으나 이 sum때문에 문제가 있었다.
지금 생각해보니 부분집합으로 풀고 4개 다 선택된 시점에 도시의 피자배달거리 구해도 될거같긴하다.
'''
def dist(h,s):
      return abs(h[0] - s[0]) + abs(h[1] - s[1])
      
def dfs(l,s): #조합은 start인덱스 필요
      global mmin
      
      if l == m:
            ssum = 0
            for h in home: #각 집마다
                  ssum += min( [ dist(h,store[s]) for s in res ] ) #뽑힌 store중에서 가장 가까운 store과의 거리 구함.
            if ssum < mmin:
                  mmin = ssum
            return

      for i in range(s, len(store)):
            if ch[i] == 0:
                  ch[i] = 1 #s 값이 있으면 ch가 필요없다. 어처피 이전 것은 선택하지 못하니까.
                  res[l] = i 
                  dfs(l+1, i+1)
                  ch[i] = 0 #s 값이 있으면 ch가 필요없다. 어처피 이전 것은 선택하지 못하니까.
            
      
n,m = map(int,input().split())
a = [ list(map(int,input().split())) for _ in range(n) ]
home = list()
store = list()

for i in range(n):
      for j in range(n):
            if a[i][j] == 1:
                  home.append((i,j))
            elif a[i][j] == 2:
                  store.append((i,j))

res = [0]*m
ch = [0]*len(store)
mmin = float("inf")
dfs(0,0)
print(mmin)

#answer
'''
집 리스트, 피자집 리스트 만들기
6개중에 4개 고르는 문제 => 6C4 조합 문제!!
본인과 풀이 똑같음.
'''
