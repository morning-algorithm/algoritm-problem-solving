import sys
#sys.stdin = open("input.txt","rt")


#me
def digit_sum(x):
    int_l = list(map(int,list(x)))
    return sum(int_l)

N = int(input())
str_numbers = input().split()

max = -1
max_number = -1
for n in range(N):
    s = digit_sum(str_numbers[n])
    if s > max:
        max = s
        max_num = str_numbers[n]
print(max_num)


'''answer
몫과 나머지를 이용하는 방법
def digit_sum(x):
    sum = 0
        while x>0:
        sum+=x%10
        x=x//10
    return sum
'''