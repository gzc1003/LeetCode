class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.string = s
        self.count = 0

        for i in range(len(s)):
            self.count_palindrom(i,i)
            self.count_palindrom(i,i+1)


        return self.count

    def count_palindrom(self,start,end):
        if start < 0 or end >= len(self.string):
            return
        s = self.string[start:end+1]
        if s == s[::-1]:
            self.count += 1
            self.count_palindrom(start-1,end+1)


s = Solution()
print(s.countSubstrings("aba"))