class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        correct = [i for i in range(1,len(nums)+1)]
        nums.sort()

        prev = 0
        for i in nums:
            if i == prev:
                first = i
            prev = i

        nums =list(set(nums))
        for i,j in enumerate(correct):
            if i==len(nums) or j != nums[i]:
                second = j
                break

        return [first,second]


s = Solution()
print(s.findErrorNums([2,3,3,4]))