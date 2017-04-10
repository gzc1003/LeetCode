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
        # divide and conquer
        self.maxlen = 0
        self.helper(root, root)
        return self.maxlen


    def helper(self, root, previous):
        if not root: return 0
        left_len = self.helper(root.left, root)
        right_len = self.helper(root.right, root)
        self.maxlen = max(self.maxlen, left_len+1, right_len+1)
        if root.val == previous.val + 1:
            return max(left_len, right_len)+1
        else:
            return 0

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
