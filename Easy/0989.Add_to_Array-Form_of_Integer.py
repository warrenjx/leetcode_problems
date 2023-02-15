class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """

        int_num = 0
        for digit in num: 
            int_num *= 10
            int_num += digit

        int_num += k

        sol = []
        while int_num > 0: 
            sol.insert(0, int_num % 10)
            int_num /= 10

        return sol