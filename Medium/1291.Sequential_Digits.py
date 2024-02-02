class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        # get the magnitude of the low digit
        mag = 0
        temp = low
        while temp >= 10: 
            temp /= 10
            mag += 1

        # set num as the lowest sequential number of the magnitude of low
        num = 10 ** mag
        for i in range(2, 2 + mag): 
            num += (i) * (10 ** (mag - i + 1))
        
        sol = []
        # calculate further sequential numbers less than high
        while num <= high:
            # check if low because the low can be higher than the lowest sequential of its magnitude
            if num >= low: 
                sol.append(num)

            # get the right 11...11 digit to increment it
            adder = 1
            for i in range(mag): 
                adder *= 10
                adder += 1

            # if you need to move up in magnitude
            if num % 10 == 9: 
                # incrememnt magnitude
                mag += 1
                # calculate new lowest sequential for the magnitude
                num = 10 ** mag
                for i in range(2, 2 + mag): 
                    num += (i) * (10 ** (mag - i + 1))
            else: 
                # if no need to change magnitude just increment
                num += adder

        return sol
