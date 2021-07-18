import sys
#sys.stdin=open("input.txt", "rt")

s=input()
stack=[]

for x in s:
    if len(stack)==0:
        stack.append(int(x))
    else :
        if x.isdecimal()==True:
            stack.append(int(x))
        else: 
            t2=int(stack.pop())# 처음 꺼낸 것이 연산자 뒤로
            t1=int(stack.pop())
            if x=='+':
                stack.append(t1+t2)
            elif x=='-':
                stack.append(t1-t2)
            elif x=='*':
                stack.append(t1*t2)
            elif x=='/':
                stack.append(t1/t2)
print(stack[0])


'''오답
res=0
first=0
for x in s:
    if len(stack)==0:
        stack.append(x)
    else :
        if x.isdecimal()==True:
            stack.append(x)
        else: # 연산에 대한 숫자의 위치를 고려하지 않았으므로 오답 !
            t=int(stack.pop())
            if res==0 and first==0:
                res+=int(stack.pop())
            if x=='+':
                res+=t
                first=1
            elif x=='-':
                res-=t
                first=1
            elif x=='*':
                res*=t
                first=1
            elif x=='/':
                res/=t
                first=1
print(res)
'''