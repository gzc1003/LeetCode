# O(n^4)

N, M = (int(i) for i in raw_input().split())
matrix = [[0] * (M + 1) for i in xrange(N + 1)]
for i in xrange(1, N + 1):
    row = (int(n) for n in raw_input().split())
    for j, n in enumerate(row,1):
        matrix[i][j] = n


def largest_submatrix(row, column):
    maximum = 0
    for i in xrange(1, row + 1):
        for j in xrange(i, row + 1):
            s = set()
            left = 1
            for right in xrange(1, column + 1):
                for k in xrange(i, j + 1):
                    while left <= right and matrix[k][right] in s:
                        remove_set(s, left, i, j)
                        left += 1
                    if left <= right:
                        s.add(matrix[k][right])
                maximum = max(maximum, (j - i + 1) * (right - left + 1))
    return maximum

def remove_set(s, column, start, end):
    for i in xrange(start, end + 1):
        if s:
            s.remove(matrix[i][column])


print largest_submatrix(N, M)