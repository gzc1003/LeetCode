class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        new_pairs = sorted(pairs, key=lambda item:item[1])

        prev_j = None
        count = 0
        start = 0
        for i,j in new_pairs:
            if prev_j is None or prev_j < i:
                count += 1
                prev_j = j

        return count


s = Solution()
print(s.findLongestChain([[1,2], [2,3], [3,4]]))
print(s.findLongestChain([[8,9],[8,10],[-3,7],[-9,9],[8,10],[1,10],[-7,3],[-3,6],[9,10],[-8,0]]))