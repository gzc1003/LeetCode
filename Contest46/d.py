#TLE
class Solution:
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length == 0: return 0

        times = [[0]*length for i in range(length)]

        for i in range(length):
            times[i][i] = 1

        offset = 1
        while offset <= length-1:
            for i in range(0,length):

                if i+offset >= length: break

                for j in range(i+1, i+offset+1):

                    if times[i][j] != 0: continue   # this line is important to make it O(n^3)

                    if s[j] == s[i]:
                        tmp_ij = times[i][j-1]
                    else:
                        tmp_ij = times[i][j-1]+1

                    for k in range(i+1, j):
                        tmp_ij = min(tmp_ij, times[i][k-1]+times[k][j])

                    times[i][j] = tmp_ij

            offset += 1


        return times[0][len(s)-1]

s = Solution()
print(s.strangePrinter("tbgtgb"))
# abbcbc


class Solution2(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '': return 0
        while True:
            flag = True
            for i in range(len(s) - 1):
                if s[i] == s[i + 1]:
                    s = s[:i] + s[i + 1:]
                    flag = False
                    break
            if flag: break
        n = len(s)
        dp = [[200] * n for i in range(n)]
        for l in range(0, n):
            for start in range(n - l):
                if l == 0:
                    dp[start][start] = 1
                else:
                    for k in range(start, start + l):
                        dp[start][start + l] = min(dp[start][start + l],
                                                   dp[start][k] + dp[k + 1][
                                                       start + l])
                    if s[start] == s[start + l]:
                        dp[start][start + l] -= 1
        return dp[0][n - 1]

# WA
class Solution3:
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length == 0: return 0

        times = [[0]*length for i in range(length)]

        for i in range(length):
            times[i][i] = 1

        offset = 1
        while offset <= length-1:
            for i in range(0,length):

                if i+offset >= length: break

                for j in range(i+1, i+offset+1):

                    if s[j] == s[i]:
                        tmp_ij = times[i][j-1]
                    else:
                        tmp_ij = times[i][j-1]+1

                    for k in range(i+1, j):
                        if s[k] == s[i]:       # 错误
                            tmp_ij = min(tmp_ij, times[i][k-1]+times[k+1][j])

                    times[i][j] = tmp_ij

            offset += 1


        return times[0][len(s)-1]

s = Solution3()
print(s.strangePrinter("tbgtgb"))
# abbcbc


# WA --> TLE
class Solution3_Correct:
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length == 0: return 0

        times = [[0]*length for i in range(length)]

        for i in range(length):
            times[i][i] = 1

        offset = 1
        while offset <= length-1:
            for i in range(0,length):

                if i+offset >= length: break

                for j in range(i+1, i+offset+1):

                    if s[j] == s[i]:
                        tmp_ij = min(times[i][j-1], times[i+1][j])
                    else:
                        tmp_ij = min(times[i][j-1]+1, times[i+1][j]+1)

                    for k in range(i+1, j):
                        if s[k] == s[i]:
                            tmp_ij = min(tmp_ij, times[i][k-1]+times[k+1][j])

                    times[i][j] = tmp_ij

            offset += 1


        return times[0][len(s)-1]

s = Solution3_Correct()
print(s.strangePrinter("tbgtgb"))


#AC
class Solution:
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length == 0: return 0

        times = [[0] * length for i in range(length)]

        for i in range(length):
            times[i][i] = 1

        offset = 1
        while offset <= length - 1:
            for i in range(0, length):

                if i + offset >= length: break

                for j in range(i + 1, i + offset + 1):

                    if times[i][j] != 0: continue

                    if s[j] == s[i]:
                        tmp_ij = min(times[i][j - 1], times[i + 1][j])
                    else:
                        tmp_ij = min(times[i][j - 1] + 1, times[i + 1][j] + 1)

                    for k in range(i + 1, j):
                        if s[k] == s[i]:
                            tmp_ij = min(tmp_ij,
                                         times[i][k - 1] + times[k + 1][j])

                    times[i][j] = tmp_ij

            offset += 1

        return times[0][len(s) - 1]


class Solution4:

    def strangePrinter(self, S):
        memo = {}
        def dp(i, j):
            if i > j: return 0
            if (i, j) not in memo:
                ans = dp(i+1, j) + 1
                for k in range(i+1, j+1):
                    if S[k] == S[i]:
                        ans = min(ans, dp(i, k-1) + dp(k+1, j))
                memo[i, j] = ans
            return memo[i, j]

        return dp(0, len(S) - 1)

s = Solution4()
print(s.strangePrinter("bbgtgb"))