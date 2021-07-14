import sys
from collections import deque
#sys.stdin = open("input.txt","rt")

#me
n = int(input())
a = deque(list(map(int,input().split())))
r = list()

def left():
    a.popleft()
    r.append('L')

def right():
    a.pop()
    r.append('R')

max = 0
while True:
    if len(a) == 1 and a[0] > max :
            max=a[0]
            left()
            break
    if a[0] > max and a[-1] > max:
        if a[0] < a[-1]:
            max=a[0]
            left()
        else:
            max=a[-1]
            right()
    elif a[0] > max :
        max=a[0]
        left()
    elif a[-1] > max :
        max=a[-1]
        right()
    else:
        break


print(len(r))
print(''.join(r))

#answer
'''
풀이: lt, rt 와 tuple이용
max 보다 크다면 값과 문자를 tuple로 묶고 후보리스트에 넣음.
후보리스트가 비었다면? break
비어있지 않다면?둘중 작은 값을 선택하여 결과 값에 붙이기.
후보리스트의 첫번째값의 문자가 L이면 lt값 증가. 아니면 rt값 증가.
후보리스트 초기화
'''
