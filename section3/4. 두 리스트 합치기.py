n1 = (int)(input())
num1 = list(map(int, input().split()))
n2 = (int)(input())
num2 = list(map(int, input().split()))

num1.sort()
num2.sort()

result = []
idx1 = idx2 = 0

'''mycode
for i in range(n1+ n2):
    if idx1 >= n1:
        for j in range(idx2, n2):
            result.append(num2[j])
        break
    elif idx2 >= n2:
        for j in range(idx1, n1):
            result.append(num1[j])
        break
    
    if num1[idx1] < num2[idx2]:
        result.append(num1[idx1])
        idx1 += 1
    else:
        result.append(num2[idx2])
        idx2 += 1'''

while idx1<n1 and idx2<n2:
    if num1[idx1] < num2[idx2]:
        result.append(num1[idx1])
        idx1 += 1
    else:
        result.append(num2[idx2])
        idx2 += 1

if idx1 < n1:
    result += num1[idx1:]
elif idx2 < n2:
    result += num2[idx2:]

for x in result:
    print(x, end=' ')
