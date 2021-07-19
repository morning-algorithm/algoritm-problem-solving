
import sys
sys.stdin = open("input.txt","rt")

#me
#입력 4번??
d = dict()
a = input()
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

b = input()

for i in a:
    if len(a) != len(b):
        print("NO")
        break
    else:
        if i in d:
            d[i] -= 1
        else:
            print("NO")
            break
else:
    for v in d.values():
        if v != 0: 
            print("NO")
            break
    else:
        print("YES")