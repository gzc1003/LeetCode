N, M, K = (int(i) for i in raw_input().split())
maximum = 0
# brute force
matrix = [[0 for i in xrange(M+1)] for j in xrange(N+1)]
for i in xrange(1,N+1):
    row = (int(n) for n in raw_input().split())
    for j, num in enumerate(row, start=1):
        matrix[i][j] = num

for i in xrange(1,N+1):
    for j in xrange(1,M+1):
        sum_matrix = [[0 for m in xrange(M + 1)] for n in xrange(N + 1)]
        for ii in xrange(i,N+1):
            for jj in xrange(j, M+1):
                sum_matrix[ii][jj] = matrix[ii][jj]+sum_matrix[ii-1][jj]+sum_matrix[ii][jj-1]-sum_matrix[ii-1][jj-1]
                if sum_matrix[ii][jj] <= K:
                    maximum = max(maximum, (ii-i+1)*(jj-j+1))

print maximum