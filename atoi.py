class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        str1 = str.strip()
        
        i = 0
        n = 0
        sign = 1
        
        if str1 == '' or (not str1[0].isdigit() and str1[0] not in '+-'):
            return 0
        else:
            if str1[0] == '+':
                sign = 1
                i += 1
            elif str1[0] == '-':
                sign = -1
                i += 1
            while i < len(str1) and str1[i].isdigit():
                n = 10*n + int(str1[i])
                i += 1
            
            n *= sign
            if n < -2147483648:
                n = -2147483648
            elif n > 2147483647:
                n = 2147483647
                
            return n
