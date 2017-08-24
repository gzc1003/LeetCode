# class Solution:
#     def imageSmoother(self, M):
#         """
#         :type M: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         if len(M) == 0: return
#
#         new_M = [[0] * len(M[0]) for i in range(len(M))]
#
#         for i, line in enumerate(M):
#             for j, num in enumerate(line):
#                 left = 0
#                 right = 0
#                 up = 0
#                 down = 0
#                 left_down = 0
#                 left_up =0
#                 right = 0
#                 right_down = 0
#                 right_up = 0
#                 cnt = 1
#
#                 if j - 1 >=0:
#                     left = M[i][j-1]
#                     cnt += 1
#                     if i - 1 >=0:
#                         left_up = M[i-1][j-1]
#                         cnt += 1
#
#                 if j + 1 < len(line):
#                     right = M[i][j+1]
#                     cnt += 1
#                     if i+1 <len(M):
#                         right_down = M[i+1][j+1]
#                         cnt += 1
#
#                 if i - 1 >= 0:
#                     up = M[i-1][j]
#                     cnt += 1
#                     if j+1 <len(line):
#                         right_up = M[i-1][j+1]
#                         cnt += 1
#
#                 if i + 1 < len(M):
#                     down = M[i+1][j]
#                     cnt += 1
#                     if j - 1 >=0:
#                         left_down = M[i+1][j-1]
#                         cnt += 1
#
#                 new_M[i][j] = (num +left +right +up +down +left_up +left_down+right_down+right_up) // cnt
#
#
#         return new_M

class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(M) == 0: return

        new_M = [[0] * len(M[0]) for i in range(len(M))]

        for i, line in enumerate(M):
            for j, num in enumerate(line):

                n = 0
                cnt = 0
                for x in [-1, 0, 1]:
                    for y in [-1, 0, 1]:
                        if 0 <= i+x <len(M) and 0 <= j+y <len(M[0]):

                            n += M[i+x][j+y]
                            cnt += 1

                new_M[i][j] = n // cnt


        return new_M


s = Solution()
print(s.imageSmoother([[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]))