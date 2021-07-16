a = input()
stack = []
result = ''
for x in a:
    if x.isdecimal():
        result += x
    else:
        if x == '(':
            stack.append(x)
        elif x=='*' or x=='/':
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
                result += stack.pop()
            stack.append(x)
        elif x=='+' or x=='-':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(x)
        elif x==')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop() #( 빼내기

while stack:
    result += stack.pop()

print(result)
                
