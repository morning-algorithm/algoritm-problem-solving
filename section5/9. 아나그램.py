import sys
#sys.stdin=open("input.txt", "r")

n1 = input()
n2 = input()

an = True

for i in range(len(n1)):
    if n1.count(n1[i]) != n2.count(n1[i]):
        an = False
        break;

if an:
    print("YES")
else:
    print("NO")
