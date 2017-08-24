class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        from math import sqrt

        for i in xrange(0, c + 1):
            j = c - i ** 2
            if j < 0:
                break
            elif j == 0:
                return True

            j = sqrt(j)
            s = str(j)
            if s[-1] == '0':
                return True

        return False
        # from math import sqrt
        #
        # for i in xrange(0,int(sqrt(c))+1):
        #     j = c - i**2
        #
        #     for k in xrange(0,int(sqrt(j))+1):
        #         if k**2 == j:
        #             return True
        #
        # return False

s = Solution()
print s.judgeSquareSum(0)
print s.judgeSquareSum(2)
print s.judgeSquareSum(4)
print s.judgeSquareSum(5)
print s.judgeSquareSum(3)
print s.judgeSquareSum(25)
print s.judgeSquareSum(24)