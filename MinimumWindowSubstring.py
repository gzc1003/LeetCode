class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        from collections import defaultdict
        count = 0
        frequency = defaultdict(int)
        ret_left = 0
        ret_right = -1

        for c in t:
            frequency[c] += 1

        left = 0
        for right in range(len(s)):
            if frequency[s[right]] > 0:
                count += 1
            frequency[s[right]] -= 1

            if count == len(t):
                while frequency[s[left]] < 0:
                    frequency[s[left]] += 1
                    left += 1

                if ret_right == -1 or right - left + 1 < ret_right - ret_left + 1:
                    ret_left = left
                    ret_right = right

        return s[ret_left:ret_right + 1]


s = Solution()
print(s.minWindow("ab", "b"))