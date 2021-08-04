import sys
#sys.stdin = open("input.txt","rt")


#me
'''
애로사항: 묶었는데, 0하나만 남게 묶이는 경우때문에 애를 먹었음
0하나만 있는 경우는 존재하지 않고, 잘못 묶은것이기 때문에 더이상 진행할 필요가 없다.
그래서 해당 레벨의 원소가 0이면 return 해준다.

풀이:
내 다음꺼까지(L+1) 묶었을때 25 이하라면 묶을 수 있으므로 묶은 뒤 갈 수 있는 원소는 L+2
'''

def dfs(L):
    global cnt
    
    if L == len(a):
        cnt += 1
        print(''.join(res))
        return

    
    if a[L] == 0:
        return

    res.append(chr(a[L]+64))
    dfs(L+1)
    res.pop()

    if L != len(a)-1 and (a[L] * 10 + a[L+1]) <= 25:
        res.append(chr(a[L] * 10 + a[L+1] + 64))
        dfs(L+2)
        res.pop()


a = list(map(int, str(input())))
cnt = 0
res = list()
dfs(0)
print(cnt)

#answer
'''마지막 원소 판별을 마지막에 -1하나 더 넣어서 편하게 해준다
답 되게 복잡하게 for문 돌려서 판별하네...'''
