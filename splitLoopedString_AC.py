class Solution(object):
    def splitLoopedString(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # O(2kn)
        new_strs = [max(astr, astr[::-1]) for astr in strs]
        max_str = ""
        for i, astr in enumerate(new_strs):
            n = len(astr)
            for astr in [astr, astr[::-1]]:
                for j in xrange(n):
                    max_str = max(max_str, astr[j:n] + ''.join(
                        new_strs[i + 1:] + new_strs[:i]) + astr[:j])

        return max_str