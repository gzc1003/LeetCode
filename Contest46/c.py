class Solution:
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return False

        if not root.left and not root.right: return False

        tree_sum = self.cal_tree_sum(root)
        self.tree_sum = tree_sum
        self.res = False

        self.postorder(root)

        return self.res

    def cal_tree_sum(self, root):
        if not root:
            return 0

        res = root.val

        res += self.cal_tree_sum(root.left)

        res += self.cal_tree_sum(root.right)

        return res

    # def postorder(self, root):
    #     if not root:
    #         return 0
    #
    #     left_sum = self.postorder(root.left)
    #     if left_sum == self.tree_sum - left_sum:
    #         self.res = True
    #
    #     right_sum = self.postorder(root.right)
    #     if right_sum == self.tree_sum - right_sum:
    #         self.res = True
    #
    #     return root.val + left_sum +right_sum


    def postorder(self, root):
        if not root:
            return 0

        res = root.val + self.postorder(root.left) + self.postorder(root.right)

        if res == self.tree_sum - res:
            self.res = True

        return res