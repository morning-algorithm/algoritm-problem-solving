import sys
#sys.stdin = open("input.txt",r)

def dfs(x):
    if dy[x] > 0:
        return dy[x]
    else:
        dy[x] = dy[x-1] + dy[x-2]
        return dy[x]

n = int(input())
dy = [0] * (n+1)
print(dfs(n))

#answer
'''
탑다운 방식은 넓은 의미에서 동적 계획법이고 (메모이제이젼해서 재귀 컷 엣지지만 뻗어나가는 방식이 점화식이랑 비슷)..
작은 문제부터 큰 문제로 확장해나가는 바텀업 방식이 진짜 동적계획법이다.
'''
