class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        start = -1
        end = -1

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                if nums[mid] == target:
                    start = mid
            print(left, right)

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                if nums[mid] == target:
                    end = mid
            print(left,right)

        return [start, end]


s = Solution()
print(s.searchRange([5,7,7,8,8,10], 8))