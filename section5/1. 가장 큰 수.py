'''my code
def make_list(n):
    tmp = str(n)
    for x in tmp:
        num.append(x)
        
num = []
n, m = map(int, input().split())
make_list(n)
idx = 0
result = 0
while result < m and idx < len(num)-1:
    if num[idx] >= num[idx+1]:
        idx += 1
    else:
        while num[idx] < num[idx+1] and result < m:
            num.pop(idx)
            result += 1
            idx -= 1
            if idx == -1:
                idx = 0
                break

for i in range(m-result):
    num.pop()

for x in num:
    print(x, end='')
'''

num, m = map(int, input().split())
num = list(map(int, str(num)))
stack = []
for x in num:
    while stack and m>0 and stack[-1] < x:
        stack.pop()
        m -= 1
    stack.append(x)

if m!= 0:
    stack = stack[:-m]
    
result = ''.join(map(str, stack))
print(result)
    
