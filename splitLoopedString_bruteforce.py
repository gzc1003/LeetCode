class Solution(object):
    def splitLoopedString(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # k is the number of strs
        # n is length of each str
        # brute force O(2^k * k * kn)

        m = 0
        for astr in strs:
            m += len(astr)

        self.strs = strs + strs
        n = len(strs)
        max_s = ['']

        for i in xrange(n):
            self.dfs(i, i + n - 1, m, max_s, [])
        return max_s[0]

    def dfs(self, start, end, m, max_s, res):
        curr_s = self.strs[start]
        for curr in [curr_s, curr_s[::-1]]:
            res.append(curr)
            if start == end:
                s = ''.join(res)
                for j in xrange(m):
                    max_s[0] = max(max_s[0], s[j:m] + s[0:j])
            else:
                self.dfs(start + 1, end, m, max_s, res)
            res.pop()


s = Solution()
print s.splitLoopedString(["abc", "xyz"])
