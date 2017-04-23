class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if len(M) == 0:
            return 0

        row = len(M)
        column = len(M[0])
        horizontal = [[0] * (column + 2) for i in xrange(row + 2)]
        vertical = [[0] * (column + 2) for i in xrange(row + 2)]
        diagonal = [[0] * (column + 2) for i in xrange(row + 2)]
        anti_diagonal = [[0] * (column + 2) for i in xrange(row + 2)]
        maximum = 0

        for i, rows in enumerate(M, 1):
            for j, digit in enumerate(rows, 1):
                if digit == 1:
                    horizontal[i][j] = horizontal[i][j - 1] + 1
                    vertical[i][j] = vertical[i - 1][j] + 1
                    diagonal[i][j] = diagonal[i - 1][j - 1] + 1
                    anti_diagonal[i][j] = anti_diagonal[i - 1][j + 1] + 1
                    maximum = max(maximum, horizontal[i][j], vertical[i][j],
                                  diagonal[i][j], anti_diagonal[i][j])

        return maximum

s = Solution()
print s.longestLine([[0,1,1,0],
 [0,1,1,0],
 [0,0,0,1]])
