# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.post_order(root)
        return self.res

    def post_order(self, root):
        if not root:
            return 0
        left_sum = self.post_order(root.left)
        right_sum = self.post_order(root.right)

        self.res +=abs(left_sum-right_sum)
        return left_sum+right_sum+root.val

s = Solution()
one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)