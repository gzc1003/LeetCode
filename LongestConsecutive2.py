# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxlen = 0
        self.helper(root, root)
        return self.maxlen

    def helper(self, root, previous):
        if not root: return (0, 0)
        li, ld = self.helper(root.left, root)
        ri, rd = self.helper(root.right, root)

        self.maxlen = max(self.maxlen, ld + ri + 1, li + rd + 1)

        ret_i = 0
        ret_d = 0
        if root.val == previous.val - 1:
            ret_d = max(ld, rd) + 1
        if root.val == previous.val + 1:
            ret_i = max(li, ri) + 1
        return (ret_i, ret_d)