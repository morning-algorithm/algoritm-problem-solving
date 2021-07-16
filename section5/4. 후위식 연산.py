import sys
#sys.stdin=open("input.txt", "r")

n = input()
st = []

for x in n:
    if x.isdecimal():
        st.append(int(x))
    else:
        n1 = st.pop()
        n2 = st.pop()
        
        if x == '+':
            st.append(n1 + n2)
        if x == '-':
            st.append(n2 - n1)
        if x == '*':
            st.append(n2 * n1)
        if x == '/':
            st.append(n2 / n1)

print(st.pop(0))
