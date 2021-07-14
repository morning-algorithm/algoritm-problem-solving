n = int(input())
num = list(map(int, input().split()))

'''my code
sequence = []
s = ""

if num[0] < num[-1]:
    s += "L"
    sequence.append(num.pop(0))
else:
    s += "R"
    sequence.append(num.pop())
    
while len(sequence) <= n:
    tmp = []
    tmp.append((num[0], 'L'))
    tmp.append((num[-1], 'R'))
    tmp.sort()
    if tmp[0][0] > sequence[-1]:
        s += tmp[0][1]
        sequence.append(tmp[0][0])
        num.remove(tmp[0][0])
    elif tmp[1][0] > sequence[-1]:
        s += tmp[1][1]
        sequence.append(tmp[1][0])
        num.remove(tmp[1][0])
    else:
        break'''

lt = 0
rt = n-1
last = 0
result = ""

while lt <= rt:
    tmp = []
    if num[lt] > last:
        tmp.append((num[lt], 'L'))
    if num[rt] > last:
        tmp.append((num[rt], 'R'))
    tmp.sort()
    if len(tmp) == 0: #아무것도 들어가지 못 함
        break
    else:
        result += tmp[0][1]
        last = tmp[0][0]
        if tmp[0][1] == 'L':
            lt += 1
        else:
            rt -= 1

print(len(result))
print(result)
