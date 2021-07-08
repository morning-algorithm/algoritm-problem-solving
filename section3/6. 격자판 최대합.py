import sys
#sys.stdin=open("input.txt", "rt")

T=int(input())
row_max=0
row_sum=0
col_sum=[0]*T
a_sum=0
b_sum=0
values=[]
for i in range(T):
    a = list(map(int, input().split()))
    for j in range(T):
        col_sum[j]+=a[j]
    a_sum+=a[i]
    b_sum+=a[T-1-i]
    row_sum=sum(a)
    if row_sum>row_max :
        row_max=row_sum
values.append(row_max)
values+=col_sum
values.append(a_sum)
values.append(b_sum)
print(max(values))