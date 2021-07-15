import sys
#sys.stdin = open("input.txt","rt")

#answer
'''
* 후위표기식: 컴퓨터에서 연산하는 방식,  **stack 필요**, 

* 풀이:
    - 숫자면 출력
    - 연산자면? 스택 필요!
        - 스택 상단에 있는 것
            - 아래있는 연산자들보다 우선순위가 더 높은 연산자. (넣으려고 할때 더 높은 연산자가 있으면 꺼내고 넣어야한다. )

        - 연산자 우선순위
            - * / > + - 
            - 같은 우선순위면 중위식에서 왼쪽에 있는 것이 더 높음

        - + - 이면? 
            - 스택에 있는 것 다 끄집어내서 출력하고 append. 왜? +-는 자기보다 낮은 우선순위가 없으므로.
            - 같은 우선순위인 -,+를 만나도 스택에 있는것 전부 출력. 왜? 이미 스택에 있는 것이 중위식 왼쪽에 있던 것으로 우선순위 더 높음.

        - * /면? 나보다 우선순위가 높은 연산자는, 같은 */가 있으면 끄집어내고 자신을 넣는다. 

        => 나와 스택에 있는 것을 비교해서 나보다 우선순위가 같거나 높으면 pop해서 출력하고 자신을 append

        - (를 고려하면?
            - 앞으로 연산자들은 ( 이후에 쌓인 괄호들만 처리함.
            - (면? 무조건 append하고 )를 만났을때 꺼냄.
            - )면? 여는 괄호 전까지에 있는 모든 연산자 꺼냄. 그리고 (를 pop
'''

a = list(input())
s = list()

for i in range(len(a)):
    if a[i] == "(":
        s.append(a[i])

    elif a[i] == ")":
        while len(s):
            if s[-1] == "(":
                s.pop()
                break
            else:
                print(s.pop(),end='')

    elif a[i] == "*" or a[i] == "/":
        while len(s):
            if s[-1] == "*" or s[-1] == "/":
                print(s.pop(),end='')
            else:
                break
        s.append(a[i])
        
    elif a[i] == "+" or a[i] == "-":
        while len(s):
            if s[-1] != "(":
                print(s.pop(),end='')
            else: 
                break
        s.append(a[i])
    else:
        print(a[i],end='')

for _ in range(len(s)):
    print(s.pop(),end='')
