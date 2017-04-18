class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = 0
        l = 0
        max_l = 0
        for i in xrange(len(s)):
            if s[i] == 'A':
                a += 1
            elif (i == 0 and s[i] == 'L') or (s[i] == 'L' and s[i - 1] != 'L'):
                l = 1
            elif i >= 1 and (s[i] == 'L' and s[i - 1] == 'L'):
                l += 1
            max_l = max(max_l,l)
        if a <= 1 and max_l <= 2:
            return True
        else:
            return False

s = Solution()
print s.checkRecord('PPALLL')