# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None: return 0

        from collections import deque

        level = deque([root])
        width = 1
        max_width = 1

        while level:
            for i in range(width):
                node = level.popleft()
                if node:
                    level.append(node.left)
                    level.append(node.right)
                else:
                    level.append(None)
                    level.append(None)

            width = len(level)

            while level and level[-1] is None:
                level.pop()
                width -= 1
            while level and level[0] is None:
                level.popleft()
                width -= 1

            max_width = max(max_width, width)

        return max_width
s = Solution()
print(s.widthOfBinaryTree())