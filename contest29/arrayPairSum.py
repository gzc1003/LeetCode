class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_nums = sorted(nums)
        res = 0
        for i in xrange(0,len(nums),2):
            res += new_nums[i]
        return res