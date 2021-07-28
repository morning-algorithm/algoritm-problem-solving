import sys
#sys.stdin = open("input.txt","rt")

n,f = map(int,input().split())

#me
''' timelimit 
def paskal():
    global pas
    while True:
        if len(pas) == 1:
            if pas[0] == f: 
                print(' '.join(map(str,res)))
                sys.exit(0)
            break
        tmp = len(pas)
        for i in range(0,tmp-1):
            pas.append(pas[i]+pas[i+1])
        pas = pas[tmp:]
    

def dfs(x):
    global pas
    if x == n:
        pas = res.copy()
        paskal()
        return
    for i in range(1,n+1):
        if ch[i] == 0:
            res[x] = i
            ch[i] = 1
            dfs(x+1)
            ch[i] = 0

cnt = 0
res = [0]*n
pas = []
ch = [0]*(n+1)
dfs(0)
'''

#answer
'''
실제로 더하는 시뮬레이션 하면 굉장히 비효율적!
미리 이항계수를 계산하여 시간복잡도를 줄인다!

   1    2    3     4
    1+2   2+3   3+4
    1+2+2+3 2+3+3+4
    1+2+2+2+3+3+3+4
= 1+ 2x3+ 3x3+ 4

=> 1x'1'+ 2x'3' + 3x'3'+ 4x'1'
=> 원소 1,2,3,4에 순서대로 1,3,3,1 곱한 값이 답.

n=3이면?
    1a^2 + 2ab+ 1b^2
    1 2 1 (이항계수)
n=4이면?
    1a^3 + 3a^2b + 3ab^2 + 1b^3
    1 3 3 1 (이항계수)
    3C0 3C1 3C2 3C3
    1 3/1 3x2/2x1 3x2x1/3x2x1
n=5면?
    1 4 6 4 1
    4C0 4C1 4C2 4C3 4C4

=> n이 입력되면 이 이항계수들을 미리 계산하여 배열에 입저얺고
paskal()함수없이 배열이용하여 바로 계산해버린다! 

'''
def dfs(x):
    global pas
    if x == n:
        s = 0
        for i in range(n):
            s += res[i]*b[i]
        if s == f:
            print(' '.join(map(str,res)))
            sys.exit(0)
        return
    for i in range(1,n+1):
        if ch[i] == 0:
            res[x] = i
            ch[i] = 1
            dfs(x+1)
            ch[i] = 0

cnt = 0
res = [0]*n
b = [1]*n #이항계수 저장용
ch = [0]*(n+1)

#이항계수 미리 계산
for i in range(1,n):
    b[i] = b[i-1] * (n-i) // i #1 3/1 3x2/2x1 3x2x1/3x2x1 앞에수에다가 계속 추가
dfs(0)


#(6-12) answer2 - 라이브러리 사용
'''
#코테에서 라이브러리 쓰지 못하게 막을 수도 있고 복잡한 조건이 있을수도 있으니기본인 dfs로 구하는 방법을 잘 알아놓기! 

import itertools as it #순열이나 조합 쉽게 구해주는 라이브러리

a = [1,2,3,4]
for tmp in it.permutations(a): #가능한 모든 순열(중복순열x)을 구해줌. it.permutations(a,3): a에서 3개뽑는 순열의 모든 경우
    sum = 0
    for L ,x in enumerate(tmp):
        sum+=(x*b[L])
'''

