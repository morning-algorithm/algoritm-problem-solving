s = input()

num = 0
for x in s:
    if x.isdecimal():
        num = num*10 + int(x)

cnt = 0
for i in range(1, num+1):
    if num % i == 0:
        cnt += 1

print(num)
print(cnt)
