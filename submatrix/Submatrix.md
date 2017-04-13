# Submatrix

## [To the Max](http://acm.zju.edu.cn/onlinejudge/showProblem.do?problemCode=1074)

```python
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

```

## [Largest Submatrix](https://vjudge.net/problem/HDU-2870)

```python
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

```

##  [MINSUB -Largest Submatrix](https://vjudge.net/problem/SPOJ-MINSUB)

```python
# O( (log10^9)*N*M )
test_cases = int(raw_input())


def find_max_area():
    left = 0
    right = 10**9
    while left <= right:
        mid = left + (right - left) // 2
        heights = [0] * (M + 1)
        maximum_area = 0
        for i in xrange(N):
            stack = []
            for j in xrange(M + 1):
                if matrix[i][j] >= mid:
                    heights[j] += 1
                else:
                    heights[j] = 0
                while stack and heights[stack[-1]] > heights[j]:
                    k = stack.pop()
                    width = j - stack[-1] - 1 if stack else j
                    maximum_area = max(maximum_area, heights[k] * width)
                stack.append(j)

        if maximum_area < K:
            right = mid - 1
        else:
            ans1 = mid
            ans2 = maximum_area
            left = mid + 1

    print ans1, ans2


for i in xrange(test_cases):
    N, M, K = (int(i) for i in raw_input().split())
    matrix = [[-1]*(M+1) for i in xrange(N)]
    for i in xrange(N):
        for j,num in enumerate(int(i) for i in raw_input().split()):
            matrix[i][j] = num
    find_max_area()

```

## [Submatrix Sum](http://www.lintcode.com/en/problem/submatrix-sum/)

```python
class Solution:
    # @param {int[][]} matrix an integer matrix
    # @return {int[][]} the coordinate of the left-up and right-down number
    def submatrixSum(self, matrix):
        # Write your code here
        O(N^3)
        for up in xrange(len(matrix)):
            dp = [0]*len(matrix[0])
            for down in xrange(up, len(matrix)):
                pre_sum = 0
                d = {0:-1}
                for column in xrange(len(matrix[0])):
                    dp[column] = dp[column]+matrix[down][column]
                    current_sum = pre_sum + dp[column]
                    if current_sum in d:
                        return [(up, d[current_sum]+1),(down,column)]
                    d[current_sum] = column
                    pre_sum = current_sum
```

## [Largest Submatrix 3](http://codeforces.com/contest/407/problem/D)最难

```python
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
```

