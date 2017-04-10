# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # dfs
        self.maxlen = 0
        self.dfs(root, 0)
        return self.maxlen


    def dfs(self, root, n):
        if not root: return

        self.maxlen = max(self.maxlen, n+1)


        if root.left and root.val + 1 == root.left.val:
            self.dfs(root.left, n+1)
        else:
            self.dfs(root.left, 0)
        if root.right and root.val + 1 == root.right.val:
            self.dfs(root.right, n+1)
        else:
            self.dfs(root.right, 0)

if __name__ == '__main__':
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)

    root = one
    root.right = three
    three.left = two
    three.right = four
    four.right = five

    s = Solution()
    assert s.longestConsecutive(root) == 3

    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    two_two = TreeNode(2)

    root = two
    root.right = three
    three.left = two_two
    two_two.left = one
    assert s.longestConsecutive(root) == 2

    assert s.longestConsecutive(None) == 0
