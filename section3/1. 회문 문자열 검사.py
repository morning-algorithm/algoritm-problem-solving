n = int(input())

for i in range(n):
    s = input()
    s = s.upper()
    #s[::-1] : s를 거꾸로 출력
    if s == s[::-1]:
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))
