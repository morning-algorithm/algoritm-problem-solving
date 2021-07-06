import sys
#sys.stdin = open("input.txt","rt")

#me
'''시간 제한 1초 통과 실패
l = [2]
N = int(input())
for i in range(3,N+1):
    for item in l:
        if i%item == 0:
            break
    else:
        l.append(i)
print(len(l))
'''

#answer
'''
<에라토스테네스 체>이용
2부터 시작하는 연속된 자연수를 미리 써 두고,처음 나타나는 수의 배수들을 모두 지우는 식으로 나아가서 소수만 남기는 방식
출처: https://53perc.tistory.com/entry/파이썬-소수-판별하기 [53Percent]

먼저 자연수1~n까지의 배열을 만들고, 원소가 0이면 1로 체크하고 그 원소의 배수를 모두 1로 변경
ex. 자연수2를 나타내는 인덱스의 원소가 0이면 1로 체크하고, 자연수 2의 배수를 나타내는 인덱스의 원소를 모두 1으로 변경(2를 약수로 갖고 있으므로)

여러 수에 대한 소수 판별에 효율적임
에라토스테네스의 체 알고리즘의 시간 복잡도는 O(NloglogN)으로 사실상 선형 시간에 동작할 정도로 빠르다.
하지만, N크기 만큼의 메모리를 저장하고 기억해야하므로 주의
출처: https://velog.io/@koyo/python-is-prime-number
'''

n = int(input())
ch = [0]*(n+1)
cnt = 0
for i in range(2,n+1):
    if ch[i] == 0:
        cnt+=1
        for j in range(i, n+1, i):
            ch[j]=1
print(cnt)
