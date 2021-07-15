import sys
#sys.stdin=open("input.txt", "rt")

inList = list(input())
st = []
before = inList[0]
sum = 0
for i in range(len(inList)):
    if inList[i] == "(":
        st.append(inList[i])
    elif inList[i] == ")" and before != inList[i]:
        st.pop()
        sum += len(st)
    elif inList[i] == ")" and before == inList[i]:
        st.pop()
        sum += 1
    before = inList[i]
    
print(sum)
