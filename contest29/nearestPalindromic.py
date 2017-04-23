class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        length = len(n)
        if length == 1:
            return str(int(n)-1)

        high = int(n[:(length+1)//2])
        candidates = []
        for cand_high in [str(i) for i in (high, high+1, high-1)]:
            candidates.append(cand_high+(cand_high if length%2 ==0 else cand_high[:-1])[::-1])

        candidates.append('9'*(length-1))
        candidates.append('1'+'0'*(length-1)+'1')

        minimum = float('inf')
        res = '0'
        num_n = int(n)
        for candidate in candidates:
            num_candidate = int(candidate)
            distance = abs(num_candidate - num_n)
            if distance != 0 and distance < minimum:
                res = candidate
                minimum = distance
            elif distance == minimum:
                res = str(min(num_candidate, int(res)))
        return res

s = Solution()
print s.nearestPalindromic("4")
print s.nearestPalindromic("123")
print s.nearestPalindromic("3499")
print s.nearestPalindromic("3900")
print s.nearestPalindromic("99")
print s.nearestPalindromic("101")
print s.nearestPalindromic("23456")

1234
