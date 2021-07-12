import sys
#sys.stdin = open("input.txt","rt")

#me
'''
테스트케이스 첫번째만 통과
풀이는 맞았으나 e초기값 설정에서 문제가 생김
e의 최대값은 max(a)지 a[n-1]*4//n 이 아님!


n,m = map(int,input().split())
a = [ int(input()) for _ in range(n)]
a.sort()
s = a[0]*4//m
e = a[n-1]*4//n
mid = (s+e) // 2 
tot = sum(list(map(lambda x:x//mid, a)))
print(s,e,tot)
while s<=e:
    if m > tot:
        print(s,e,tot)
        e = mid - 1
        mid = (s+e) // 2 
        tot = sum(list(map(lambda x:x//mid, a))) #mid가 크면 tot가 작아진다 => e를 줄여 mid를 줄여야함
        
    elif m <= tot:
        print(s,e,tot)
        s = mid + 1
        mid = (s+e) // 2 
        tot = sum(list(map(lambda x:x//mid, a)))
print(mid)
'''

#answer
'''
* 결정 알고리즘 => 이분검색 사용
특징: 시작, 끝 범위가 정해져 있는 경우
방법: 중앙값이 답으로써 유효한지 검사 => 범위를 좁혀서 절반 날리고 더 좋은 답을 찾아서 좁혀나감. 

풀이:
최대 랜선길이 범위: 1~1000(입력받은 가장 큰 랜선길이 802 보다 넉넉히 잡아도 상관 없음)

1~1000 ,중앙: 500, 모든 랜선에 500을 나눈 몫을 더했을 때 11보다 큰지 검사 => 작음, 유효하지 않음
1~499, 중앙: 250, 모든 랜선에 250을 나눈 몫이 11보다 큰지 검사 => 작음, 유효하지 않음 
1~249, 중앙: 125, 모든 랜선에 125을 나눈 몫이 11보다 큰지 검사 => 큼. 유효함. 일단 답으로 저장 
126~249, 중앙: 187, 모든 랜선에 187을 나눈 몫이 11보다 큰지 검사 => 큼, 유효함, 일단 답으로 저장
187~249 ... 이렇게 계속 이분검색을 반복해나가면 가장 좋은 값을 찾게 됨.
'''

n,m = map(int,input().split())
a = [ int(input()) for _ in range(n)]
s = 1
e = max(a)

res = 0
while s<=e:
    mid = (s+e) // 2 
    if m <= sum(list(map(lambda x:x//mid, a))):
        res = mid
        s = mid + 1
        
    else:
        e = mid - 1
print(res)
