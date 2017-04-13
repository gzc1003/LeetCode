N, M, K = (int(i) for i in raw_input().split())

# O(N^2 * M)

matrix = [[0 for i in xrange(M+1)] for j in xrange(N+1)]
for i in xrange(1,N+1):
    row = (int(n) for n in raw_input().split())
    for j, num in enumerate(row, 1):
        matrix[i][j] = matrix  [i-1][j]+num

maximum = 0
for i in xrange(1,N+1):
    for j in xrange(i,N+1):
        pre_sum = 0
        pre_k = 1
        for k in xrange(1,M+1):
            current_sum = pre_sum + matrix[j][k] - matrix[i-1][k]
            while pre_k <= k and current_sum > K:
                current_sum -= (matrix[j][pre_k]-matrix[i-1][pre_k])
                pre_k += 1
            pre_sum = current_sum
            if pre_k <= k:
                maximum = max(maximum, (j-i+1)*(k-pre_k+1))
if maximum == 0:
    maximum = -1
print maximum

