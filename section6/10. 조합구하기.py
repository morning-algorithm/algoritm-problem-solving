import sys
#sys.stdin = open("input.txt","rt")


#me
def dfs(L):
    global cnt
    if L == m:
        print(' '.join(map(str,res)))
        cnt += 1
        return
    for i in range(1,n+1):
        if ch[i] == 0:
            if (L > 0 and res[L-1] < i) or L == 0: #전 레벨에서 선택된 것 보다 커야지 조합!
                res[L] = i 
                ch[i] == 1 #answer: 중복체크 필요없음!!!!!!! 어처피 다음 레벨의 가지는 자기보다 큰 수부터 시작하니까!!!!!! 
                dfs(L+1) 
                ch[i] == 0

n, m = map(int,input().split())
res = [0]*m
ch = [0] * (n+1)
cnt = 0
dfs(0)
print(cnt)

#answer
'''
조합 구하기 문제 굉장히 중요!
조합을 기반으로 해서 응용문제 굉장히 많이 나온다.

* 풀이:
    상태트리
    D(L,s) : D(레벨, !!!!가지를 뻗을때 갈 수 있는 제일 작은 숫자!!!!)

                  D(0,1)
           1     2     3     4
         D(1,2)
       2   3   4
    D(2,3)

* 구현:

def dfs(L,s):
    global cnt
    if L == m:
        print(' '.join(map(str,res)))
        cnt += 1
        return
    else:
        for i in range(s,n+1):
            res[L] = i
            dfs(L+1, i+1) #중복체크 필요없음!!!!!!! 어처피 다음 레벨의 가지는 자기보다 큰 수부터 시작하니까!!!!!! 
'''
    


