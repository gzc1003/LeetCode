# O(n^3)

N, M = (int(i) for i in raw_input().split())
matrix = [[0] * (M + 1) for i in xrange(N + 1)]
for i in xrange(1, N + 1):
    row = (int(n) for n in raw_input().split())
    for j, n in enumerate(row,1):
        matrix[i][j] = n

num_to_column = [{} for i in xrange(N+1)]
left_bound = [[0]*(N+2) for i in xrange(N+2)]
maximum = 0


for column in xrange(1, M+1):
    for up in xrange(N, 0, -1):
        for down in xrange(up, N+1):
            if up != down and matrix[up][column] == matrix[down][column]:
                left_bound[up][down] = column
            left_bound_tmp1 = max(num_to_column[down].get(matrix[up][column],0), left_bound[up][down-1])
            left_bound_tmp2 = max(num_to_column[up].get(matrix[down][column],0), left_bound[up+1][down])
            left_bound[up][down] = max(left_bound[up][down], left_bound_tmp1, left_bound_tmp2)

            maximum = max(maximum, (down-up+1)*(column - left_bound[up][down]))
    for row in xrange(1,N+1):
        num_to_column[row][matrix[row][column]] = column

print maximum