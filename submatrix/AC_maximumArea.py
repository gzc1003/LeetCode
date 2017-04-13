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
