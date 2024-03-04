class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        # edge case, no tokens
        if not tokens: 
            return 0

        # sort tokens so can greedily choose which to take
        tokens.sort()
        
        # unable to play any token at the start
        if tokens[0] > power: 
            return 0

        # must play the first token at the start
        power -= tokens[0]
        score = 1
        
        # have pointers to what tokens to play in what direction
        up = 1
        down = len(tokens) - 1

        while up < down: 
            if power >= tokens[up]: # greedily flip tokens face up whenever possible
                power -= tokens[up]
                score += 1
                up += 1
            elif score > 0: # only flip token down when absolutely need to
                power += tokens[down]
                score -= 1
                down -= 1
            else: 
                break

        if power >= tokens[down]: # if last token can be played face up
            return score + 1
        else: 
            return score
