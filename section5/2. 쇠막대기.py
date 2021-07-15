
import sys
sys.stdin = open("input.txt","rt")

#me
'''
여는괄호가 레이저인지 아닌지 구분하는 변수를 씀.
처음 스택에 삽입될땐 가능성을 열어둬 레이저여부가 true이고, 해당 괄호가 진짜 레이저였다면 그 이전의 여는 괄호들은 모두 레이저가 아님. 

닫는 괄호는
- 지금 여는 괄호가 레이저라면 그 앞에 있는 모든 괄호를 잘라야 하므로 그만큼 cnt를 증가
- 지금 여는 괄호가 레이저가 아니라면 막대기가 끝난 것이므로 단순히 cnt+=1 
'''
a = list(input())
s = list()
is_laser = True
cnt = 0 

for item in a:
    if item == '(':
        s.append(item)
        is_laser = True
    else: # item == ')'
        if is_laser == True:
            s.pop()
            cnt += len(s)
            is_laser = False
        else:
            s.pop()
            cnt += 1
print(cnt)

#answer
'''
* 아이디어: 
여는괄호가 들어왔을 때 레이저인지 쇠막대기인지모름.
 - 근데 그다음에 여는 괄호가 들어온다면 그 이전꺼는 쇠막대기가 됨.
 - 근데 그다음에 닫는 괄호가 들어온다면 그 이전꺼는 레이저임. 자르기

닫는 괄호가 들어왔을때 그 앞에 닫는 괄호가 있다면?
 - 쇠막대기의 끝임. 카운팅.

 * 풀이:
스택을 사용하여 구현
- 여는 괄호는 무조건 스택에 append
- 닫는 괄호가 나왔을때 
    - 앞에 것이 여는 괄호면? pop, 스택 길이만큼 여는괄호가 쌓여있으니 그만큼 증가
    - 앞에 것이 닫는 것이면? 스택에서 pop하고 cnt += 1

답안에서는 is_laser 사용하지 않고 자신의 전 아이템인 a[i-1]이 닫는괄호인지 여는 괄호인지 검사하는 방법을 씀.

for i in range(len(s)):
    if s[i]=='(':
        stack.append(s[i])
    else:
        stack.pop()
        if s[i-1]=='(':
            cnt+=len(stack)
        else:
            cnt+=1
'''
