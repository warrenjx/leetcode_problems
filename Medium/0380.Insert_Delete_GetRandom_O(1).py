class RandomizedSet(object):
    def __init__(self):
        # dictionary for O(1) lookup
        self.map = {}
        # array for random selection
        self.arr = []
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.map: 
            # add term to end of array and idx to dictionary
            self.map[val] = len(self.arr)
            self.arr.append(val)

            return True
        else: 
            return False
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.map:
            # get last term index
            back = len(self.arr) - 1 
            if self.map[val] == back:
                # if term at end just pop and remove
                self.arr.pop()
                del self.map[val]
            else: 
                # if not at end, swap with end term
                self.arr[self.map[val]] = self.arr[back]
                self.map[self.arr[back]] = self.map[val]
                # pop and remove end term
                self.arr.pop()
                del self.map[val]

            return True
        else: 
            return False


    def getRandom(self):
        """
        :rtype: int
        """
        # find random idx
        idx = randint(0, len(self.arr) - 1)
        # return random term at idx
        return self.arr[idx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
