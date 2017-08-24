class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        maximum = sum(nums[0:k])
        prev = sum(nums[0:k])
        for i in xrange(1,len(nums)-k+1):
            if prev-nums[i-1]+nums[i+k-1] > maximum:
                maximum = prev-nums[i-1]+nums[i+k-1]
            prev = prev-nums[i-1]+nums[i+k-1]

        return maximum / k

s = Solution()
print s.findMaxAverage([0,1,1,3,3], 4)