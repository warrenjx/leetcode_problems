class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        # holds array of: [(length of word, word itself)]
        lens = [] 

        for word in words: 
            lens.append((len(word), word))

        rows = [] # holds the list of words in each row
        space_lens = [] # holds the amount of spaces to be in each row

        # used for iteratively filling rows and space_lens
        curr = []
        curr_len = 0
        raw_len = 0

        # fill in rows and space_lens
        for w_len, word in lens: 
            if curr_len + w_len >= maxWidth + 1: # if new row is needed
                rows.append(curr)
                space_lens.append(maxWidth - raw_len)

                # reset the variables to current word values
                curr = [(w_len, word)]
                curr_len = w_len + 1
                raw_len = w_len
            else: # add to current row
                curr.append((w_len, word))
                curr_len += w_len + 1
                raw_len += w_len
        
        # add in the last row
        rows.append(curr)
        space_lens.append(maxWidth - raw_len)

        sol = []

        # convert rows to strings
        for i in range(len(rows) - 1): 
            curr_row = ""

            # calculate the minimum space between words
            min_space = -1
            if len(rows[i]) > 1: 
                min_space = space_lens[i] // (len(rows[i]) - 1)
            
            # calculate the amount of words which will have extra space after them
            extra_thresh = space_lens[i] - ((len(rows[i]) - 1) * min_space)

            for j in range(len(rows[i]) - 1): 
                curr_row += rows[i][j][1] # add word

                for k in range(min_space): # add mininum required spaces after each word
                    curr_row += " "
                if j < extra_thresh: # add extra space if below extra space threshold
                    curr_row += " "
            
            # special case for last word
            if len(rows[i]) > 1: # add it in at end, no spaces after it
                curr_row += rows[i][-1][1]
            else: # special case for single word lines
                curr_row += rows[i][-1][1] # add word

                for i in range(space_lens[i]): # add spaces to fill the line
                    curr_row += " "

            # add final word to line
            sol.append(curr_row)
        
        # special case for last row
        last_row = ""
        for i in range(len(rows[-1]) - 1): 
            last_row += rows[-1][i][1]
            last_row += " "
        
        last_row += rows[-1][-1][1]

        # add filler spaces to last row
        for i in range(space_lens[-1] - (len(rows[-1]) - 1)): 
            last_row += " "
        
        sol.append(last_row)

        return sol
