class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict

        d = defaultdict(lambda: 0)
        maximum = 0

        for row in wall:
            key = 0
            for i in row[:-1]:
                key += i
                d[key] += 1
                if d[key] > maximum:
                    maximum = d[key]

        return len(wall) - maximum

s = Solution()
b = [[1,2,2,1],
 [3,1,2],
 [1,3,2],
 [2,4],
 [3,1,2],
 [1,3,1,1]]
print s.leastBricks(b)

