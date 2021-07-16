
import sys
#sys.stdin = open("input.txt","rt")

#me
''' p2와 p1을 나눈 이유는 -와 /때문. 피연산자 순서가 있다 ''' 
a = list(input())
s = list()

for item in a:
    if item.isdecimal():
        s.append(int(item))
    else: 
        p1 = s.pop()
        p2 = s.pop()
        if item == '+':
            s.append(p2 + p1)
        elif item == '-':
            s.append(p2 - p1)
        elif item == '*':
            s.append(p2 * p1)
        elif item  == '/':
            s.append(p2 / p1)

print(s.pop())

#answer
''' 
* 후위식 연산:
    - 컴퓨터가 편한 방법. 그래서 후위식으로 바꾸는 것.
    - 앞에서부터 탐색을하다가 연산자를 만나면, 앞에 두개의 피연산자로 연산하여 결과물이나옴.
    - '-' 나 '/'는 앞 피연산자에서 뒤 피연산자를 뺀다
        - 왜? 5-3은 후위식으로 53-이다. 피연산자의 순서는 바뀌지 않는다는 것 명심하기!

*풀이: 
    - **stack**을 사용!
'''