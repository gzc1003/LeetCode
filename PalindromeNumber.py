class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """ 
        if x < 0:
            return False
            
        div = 1
        while x // div > 9:
            div *= 10
        
        while x != 0:
            left = x % 10
            right = x // div 
            if left != right:
                return False
            x = (x % div) // 10
            div /= 100
            
        return True
