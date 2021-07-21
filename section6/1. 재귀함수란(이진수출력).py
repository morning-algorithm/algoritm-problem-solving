import sys
#sys.stdin = open("input.txt","rt")

#me
'''
10진수를 2진수로 바꾸는 방법. 2로 나누면서 나머지를 기록.
몫이 0이되면 기록한 나머지를 거꾸로 적는다.
출처: https://meaningone.tistory.com/606 '''
def dfs(x):
    if x != 0:
        dfs(x // 2)
        print(x % 2, end="")

n = int(input())
dfs(n)
