import sys
#sys.stdin=open("input.txt", "rt")

T=int(input())
ox=list(map(int, input().split()))
score=0#득점, 전체 점수
t_score=0#배점

for i in range(T):
    if ox[i]==1:
        t_score+=1
        score+=t_score
    else:
        t_score=0

print(score)