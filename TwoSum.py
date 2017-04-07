class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        buffer_dict = {}
        for i in range(len(nums)):
            if nums[i] in buffer_dict:
                return [buffer_dict[nums[i]], i]
            else:
                buffer_dict[target-nums[i]] = i
        
        
        
