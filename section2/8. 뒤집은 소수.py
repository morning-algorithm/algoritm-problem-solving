import sys
#sys.stdin = open("input.txt","rt")

#me
'''x 가 1일때를 검사해주지 않아 틀렸었음!
def isPrime(x):
    ch = [0]*(x+1) #1이 되면 검사했다는 표시.
    for i in range(2,x):
        if ch[i] == 0:
            if x % i == 0:
                return False
            else:
                for j in range(i, x+1, i):
                    ch[j]=1
    return True


def reverse(str_x):
    return int(str_x[::-1].rstrip('0'))

N = int(input())
l = input().split()
for item in l:
    r = reverse(item)
    if isPrime(r) == True:
        print(r,end=' ')
'''

#answer
'''
풀이1: 해당숫자의 절반까지만 확인하는 방법
1과 자기 자신을 제외한 모든 약수는 그 수의 절반보다 작다는 사실을 이용
시간복잡도 O(N)

풀이2: 해당 숫자의 √N 까지 확인하는 방법이다
모든 약수가 가운데 약수를 기준으로 곱셈 연산에 대해 대칭을 이루는 것을 알 수 있다.
1:80, 2:40, 4:20, 5:16, 8:10. √80의 값은 대략 8.xxx의 값
약수들의 곱으로 봤을때 루트를 씌운 값이 중간값이 된다.
2에서부터 √N의 값까지 검색을한다며 이후의 값은 확인할 필요가 없게 된고 시간복잡도는 O(√N)
ex. int(number ** 0.5) + 1

출처: https://myjamong.tistory.com/139
'''
def isPrime(x):
    if x == 1:
        return False
    #풀이 1 방법 사용
    for i in range(2, x//2+1):
        if x%i == 0:
            return False
    else:
        return True

def reverse(str_x):
    return int(str_x[::-1].rstrip('0'))

N = int(input())
l = input().split()
for item in l:
    r = reverse(item)
    if isPrime(r) == True:
        print(r,end=' ')
