class Solution(object):
    # union-find version
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        count = len(M)
        students = [i for i in xrange(len(M))]

        for i, row in enumerate(M):
            for j, column in enumerate(row):
                if column == 1 and students[i] != students[j] and i != j:
                    count -= 1
                    tmp_i = students[i]
                    for k, student in enumerate(students):
                        if student == tmp_i:
                            students[k] = students[j]

        return count

    # dfs version
    def findCircleNum_dfs(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        visited = []
        count = 0
        for i,row in enumerate(M):
            if i not in visited:
                self.dfs(i, M, visited)
                count += 1
        return count

    def dfs(self, n, M, visited):
        for i, value in enumerate(M[n]):
            if value and i != n and i not in visited:
                visited.append(i)
                self.dfs(i,M,visited)


s = Solution()
print s.findCircleNum_dfs([[1,1,0],[1,1,0],[0,0,1]])