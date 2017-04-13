# O(N*M)
N, M = (int(i) for i in raw_input().split())
a = [0] * (M+1)
b = [0] * (M+1)
c = [0] * (M+1)


def helper(stack, index, array):
    global maximum
    while len(stack)>=1 and array[stack[-1]] > array[index]:
        i = stack.pop()
        maximum = max(maximum, (index - stack[-1]-1) * array[i])
    stack.append(index)



maximum = 0
for i in xrange(N):
    stack_a = [-1]
    stack_b = [-1]
    stack_c = [-1]
    for j, char in enumerate(raw_input()+'k'):
        if char == 'a' or char == 'w' or char == 'y' or char == 'z':
            a[j] += 1
        else:
            a[j] = 0
        if char == 'b' or char == 'w' or char == 'x' or char == 'z':
            b[j] += 1
        else:
            b[j] = 0
        if char == 'c' or char == 'x' or char == 'y' or char == 'z':
            c[j] += 1
        else:
            c[j] = 0
        helper(stack_a, j, a)
        helper(stack_b, j, b)
        helper(stack_c, j, c)

print maximum
