import sys
#sys.stdin=open("input.txt", "rt")

n =input()
st=[]
ans = ""

'''
for x in a:
    if x.isdecimal():
        res+=x
    else:
        if x=='(':
            st.append(x)
        elif x=='*' or x=='/':
            while len(st) > 0 and (st[-1]=='*' or st[-1]=='/'):
                res+=st.pop()
            st.append(x)
        elif x=='+' or x=='-':
            while len(st) > 0 and st[-1]!='(':
                res+=st.pop()
            st.append(x)
        elif x==')':
            while len(st) > 0 and st[-1]!='(':
                res+=st.pop()
            st.pop()
            
while len(st) > 0:
    ans+=st.pop()
print(ans)


'''



