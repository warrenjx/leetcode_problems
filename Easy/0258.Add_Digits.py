class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # repeatedly calculate new num until it is 1 digit
        while num >= 10: 
            new_num = 0
            
            # find sum of its digits with a loop
            while num > 0: 
                new_num += num % 10
                num /= 10
            
            num = new_num
        
        return num
