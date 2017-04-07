# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        root_node = ListNode(0)
        res = root_node
        
        while l1 or l2 or carry:
            l1_value = 0
            l2_value = 0
            
            if l1:
                l1_value = l1.val
                l1 = l1.next
            if l2:
                l2_value = l2.val
                l2 = l2.next

            x = l1_value + l2_value + carry
            
            root_node.next= ListNode(x % 10)
            carry = x // 10
            root_node = root_node.next
            
        return res.next
            
            
