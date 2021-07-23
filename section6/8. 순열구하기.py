import sys
#sys.stdin = open("input.txt","rt")

#me
'''
분석:
상태트리 구성!
각 원소는 간선이된다. 
이중 M개를 뽑아서 나열하는 것이니까 레벨은 뽑은 갯수이다.
한번 뽑았던 원소는 다음레벨에서 다시 뽑으면 안되니까 제거시킨다. => 전역 변수 리스트이용
'''

def dfs(L):
    global cnt
    if L == m:
        print(' '.join(map(str,s)))
        cnt +=1
        return
    for i in range(len(a)):
        #나로부터 호출되는 다음레벨에서 다시 뽑으면 안되니까 pop
        #그리고 그걸 s에 넣어 자신을 기록 (뽑은개수가 m이랑 같아질때 쌓였던 기록 출력) 
        s.append(a.pop(i)) 
        dfs(L+1)
        #이제 나로부터 호출되는 것 더이상 없으므로 기록 삭제
        #다른곳에서다시 뽑을 수 있도록 insert
        a.insert(i,s.pop())

n,m = map(int,input().split())
a = list(range(1,n+1))
s = list()
cnt = 0
dfs(0)
print(cnt)

#answer
'''
중복순열문제와 비슷하지만
중복을 하지 않도록 !!!!!!!체크리스트를 만들어서!!!!!!!! 그 가지로는 못가도록 커트.

res = [0]*n #각레벨에서 사용한 원소 저장용
ch = [0]*(n+1) 세팅

dfs:
    for i in 모든 가지 리스트:
        if ch[i] == 1 :
            이미 쓴 원소. 중복이니까 가지 cut
        else:
            들어가기전에 ch[i] = 1로 만들고
            res[레벨] = i  
            dfs(레벨+1)
            !!!!!!!!!!나온후에 ch[i] = 0 로 다시 되돌려야한다.!!!!!!!!!!       
'''
