class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [int(char) for char in str(n)]
        stack = []
        new_nums = []
        for i in xrange(len(nums) - 1, -1, -1):
            if not stack or nums[stack[-1]] <= nums[i]:
                stack.append(i)
            else:
                while stack and nums[stack[-1]] > nums[i]:
                    num = nums[stack.pop()]
                    new_nums.insert(0, num)
                new_nums.insert(1, nums[i])
                while stack:
                    new_nums.insert(1, nums[stack.pop()])
                break
        else:
            return -1
        nums = nums[:i] + new_nums

        res = 0
        for n in nums:
            res = 10 * res + n
        return res if res <= 2 ** 31 - 1 else -1