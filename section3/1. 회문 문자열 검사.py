import sys
#sys.stdin=open("input.txt", "rt")

n = int(input())
word = ['']*n

for i in range(n):
    word[i] = input()

for i in range(n):
    word[i] = word[i].upper()
    tmp = word[i][::-1]

    if word[i] == tmp:
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))
