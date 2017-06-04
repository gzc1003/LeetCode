class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        flowerbed.insert(0, 0)
        flowerbed.append(0)
        m = 0
        for i, planted in enumerate(flowerbed[1:-1], 1):
            if not planted and not flowerbed[i-1] and not flowerbed[i+1]:
                m += 1
                flowerbed[i] = 1
        return n <= m


s = Solution()
print s.canPlaceFlowers([0,0,1,0,0],2)