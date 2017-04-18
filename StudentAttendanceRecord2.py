class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

        dp = [1] * max(n + 1, 4)
        dp[1] = 2
        dp[2] = 4
        dp[3] = 7
        for i in xrange(4, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % (10 ** 9 + 7)

        res = dp[n]
        for i in xrange(n):
            res = (res + dp[i] * dp[n - i - 1] % (10 ** 9 + 7)) % (10 ** 9 + 7)

        return res