class Solution:
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        from collections import defaultdict
        times = defaultdict(int)
        tails = defaultdict(int)

        for i in nums:
            times[i] += 1


        for i in nums:
            if times[i] == 0:
                continue
            elif tails[i] > 0:
                tails[i] -= 1
                tails[i+1] += 1
            elif times[i+1] > 0 and times[i+2] > 0:
                times[i+1] -= 1
                times[i+2] -= 1
                tails[i+3] += 1
            else:
                return False
            times[i] -= 1
        return True

s = Solution()
s.isPossible([1,2,3,3,4,5])


class Solution:
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        from collections import defaultdict
        times = defaultdict(int)
        prev = None
        for i in nums:
            times[i] += 1


        for i in nums:
            if times[i] == 0:
                continue

            n = 0
            for j in range(i,nums[-1]+1):
                tmp = times[j]
                times[j] -= 1
                n += 1
                if times[j+1] == 0 or tmp > times[j+1]:
                    break

            if n < 3:
                return False

        return True

s = Solution()
print(s.isPossible([2,2,3,3,3,4,4,4,5,5]))