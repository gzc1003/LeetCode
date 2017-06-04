# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ""
        return self.helper(t)

    def helper(self, t):

        left = ""
        right = ""

        if not t.left and t.right:
            left = "()"
        elif t.left:
            left = "("+self.helper(t.left)+")"

        if t.right:
            right = "("+self.helper(t.right)+")"

        return str(t.val)+left+right