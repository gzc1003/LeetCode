class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = [[]]
        for n in nums:
            tmp_res = []
            for m in res:
                for i in xrange(len(m)+1):
                    tmp_m = list(m)
                    tmp_m.insert(i,n)
                    # if tmp_m not in tmp_res:
                    tmp_res.append(tmp_m)
            res = tmp_res

        return res

    def permute_recur(self, nums):
        res = []
        return res

s = Solution()
print s.permute([1,2,3])