import sys
#sys.stdin=open("input.txt", "rt")

n, m = input().split()
n = list(n)
m = int(m)
count = 0
st = []

for i in range(len(n)):

    while len(st) != 0 and count < m and st[len(st)-1] < n[i]:
        st.pop()
        count += 1
    st.append(n[i])

if (m-count) != 0:
    ans = "".join(st[:-(m-count)])
else:
    ans = "".join(st)

print(ans)


'''
n = list(n)
m = int(m)
count = 0;
i = 0

for i in range(len(n)):
    for j in range(1, m-count+1):
        if n[i] < n[i+j] and count < m:
           n.pop(i)
           count += 1


print("".join(n))

'''
            
        
