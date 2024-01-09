class Solution(object):
    def discountPrices(self, sentence, discount):
        """
        :type sentence: str
        :type discount: int
        :rtype: str
        """
        # turn sentence into list of words
        toks = sentence.split(' ')

        # check each word for prices
        for i in range(len(toks)): 
            # if a valid price format
            if toks[i][0] == '$' and (toks[i][1:]).isnumeric(): 
                # get numeric price
                price = float(toks[i][1:])
                # apply discount
                price -= (float(discount) / 100) * price
                # replace with discounted price
                toks[i] = "${:.2f}".format(price)

        # return tokens back to string
        return ' '.join(toks)
        
