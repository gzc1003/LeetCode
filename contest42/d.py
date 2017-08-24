class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        self.roots = sorted(dict, key=lambda s:len(s))
        words = sentence.split()
        ret = []
        for word in words:
            r = self.is_succecsor(word)
            if r:
                ret.append(r)
            else:
                ret.append(word)

        return ' '.join(ret)

    def is_succecsor(self, word):
        for root in self.roots:
            if word[:len(root)] == root:
                return root
        return False


s = Solution()
print(s.replaceWords(["cat", "bat", "rat"],
                     "the cattle was rattled by the battery"))