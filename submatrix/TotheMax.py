# O(N^2*M)
N= int(raw_input())
M=N
matrix = [ [0]*(M+1) for i in xrange(N+1)]

i = 1
j = 1
while True:
    try:
        row = (int(n) for n in raw_input().split())
        for n in row:
            matrix[i][j] = matrix[i-1][j] + n
            j += 1
            if j > N:
                j = 1
                i += 1
    except EOFError:
        break

maximum = 0
for i in xrange(1, N+1):
    for j in xrange(i, N+1):
        pre_max = 0
        for k in xrange(1, M+1):
            current = matrix[j][k]-matrix[i-1][k]
            maximum = max(maximum, current+pre_max, current)
            pre_max = max(current, pre_max + current)

print maximum
