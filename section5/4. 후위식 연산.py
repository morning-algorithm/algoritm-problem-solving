s = input()
stack = []

for x in s:
    if x.isdecimal():
        stack.append(int(x))
    else:
        second = stack.pop()
        first = stack.pop()
        result = 0
        if x == '+':
            result = first + second
        elif x == '-':
            result = first - second
        elif x == '*':
            result = first * second
        elif x == '/':
            result = first / second
        stack.append(result)

print(stack.pop())
