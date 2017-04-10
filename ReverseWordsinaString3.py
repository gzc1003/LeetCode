class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        new_words = []
        for word in words:
            new_words.append(word[::-1])

        res = ' '.join(new_words)
        return res

s = Solution()
print s.reverseWords("Let's take LeetCode contest")
print s.reverseWords("a ")