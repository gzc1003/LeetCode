# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def upside_down(root):
    res = root
    while res.left:
        res = res.left
    helper(root)
    return res


def helper(root):
    if root.left:
        new_root = helper(root.left)
        new_root.left = root.right
        new_root.right = root
        root.left = None
        root.right = None
    return root

