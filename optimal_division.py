class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        n = len(nums)
        min_dp = [[1001.0] * n for i in xrange(n)]
        max_dp = [[0.0] * n for i in xrange(n)]
        min_k = [[None] * n for i in xrange(n)]
        max_k = [[None] * n for i in xrange(n)]
        for i, num in enumerate(nums):
            min_dp[i][i] = float(num)
            max_dp[i][i] = float(num)
        for l in xrange(2, n + 1):
            for i in xrange(n - l + 1):
                j = i + l - 1
                for k in xrange(i, j):
                    if min_dp[i][k] / max_dp[k + 1][j] < min_dp[i][j]:
                        min_dp[i][j] = min_dp[i][k] / max_dp[k + 1][j]
                        min_k[i][j] = k
                    if max_dp[i][k] / min_dp[k + 1][j] > max_dp[i][j]:
                        max_dp[i][j] = max_dp[i][k] / min_dp[k + 1][j]
                        max_k[i][j] = k
        return self.construct(0, max_k[0][n - 1], n - 1, min_k, max_k, nums, 1)

    def construct(self, i, k, j, min_k, max_k, nums, flag):
        if i == j:
            return str(nums[i])
        if flag:
            s1 = self.construct(i, max_k[i][k], k, min_k, max_k, nums, 1)
            s2 = self.construct(k + 1, min_k[k + 1][j], j, min_k, max_k, nums, 0)
        else:
            s1 = self.construct(i, min_k[i][k], k, min_k, max_k, nums, 0)
            s2 = self.construct(k + 1, max_k[k + 1][j], j, min_k, max_k, nums, 1)
        if k + 1 != j:
            s2 = '(' + s2 + ')'
        return s1 + '/' + s2


s = Solution()
print s.optimoptimal_division.pyalDivision([1000,100,10,2])
