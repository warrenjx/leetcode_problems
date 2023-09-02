# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        hi = n
        lo = 0

        while lo <= hi:
            mid = (hi + lo) // 2

            res = guess(mid)

            if res > 0: 
                lo = mid + 1
            elif res < 0: 
                hi = mid - 1
            else: 
                return mid

        return lo
