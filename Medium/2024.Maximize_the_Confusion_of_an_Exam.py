class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """
        # counters for the amount of T and F in the interval
        t = 0
        f = 0

        sol = 0

        end = 0
        for i in range(len(answerKey)): 
            # increment the counters
            if answerKey[i] == "T": 
                t += 1
            else: 
                f += 1

            # shrink the window until all the Ts can be Fs or vice versa
            while min(t, f) > k: 
                if answerKey[end] == "T": 
                    t -= 1
                else: 
                    f -= 1
                
                end += 1

            sol = max(sol, i - end + 1)
        
        return sol
