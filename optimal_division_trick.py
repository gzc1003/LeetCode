class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # O(n)
        if len(nums) == 1:
            return str(nums[0])
        elif len(nums) == 2:
            return str(nums[0]) + '/' + str(nums[1])
        else:
            res = str(nums[0]) + '/' + '(' + str(nums[1])
            for n in nums[2:]:
                res += '/' + str(n)
            return res + ')'
