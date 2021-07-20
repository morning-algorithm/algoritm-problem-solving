import sys
#sys.stdin=open("input.txt", "r")

n = int(input())
word = []
write =[]

for i in range(n):
    word.append(input())

for i in range(n-1):
    w = input()
    for j in range(len(word)):
        tmp = word.pop(0)
        if w != tmp:
            word.append(tmp)
        else:
            break;

print(word.pop())


