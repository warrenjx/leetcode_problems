class TimeMap(object):

    def __init__(self):
        self.hashtable = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        # put stuff in hashtable in form of key => [(timestamp, value), ...]
        if key in self.hashtable: 
            self.hashtable[key].append((timestamp, value))
        else: 
            self.hashtable[key] = [(timestamp, value)]


    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        # if key has not be set before
        if key not in self.hashtable: 
            return ""

        stamps = self.hashtable[key]

        # if there are no sets to a key
        if len(stamps) == 0: 
            return ""
        
        # binary search the timestamps for the best fit key
        l = 0
        r = len(stamps) - 1
        while l <= r: 
            mid = (l + r) // 2

            if stamps[mid][0] == timestamp: 
                return stamps[mid][1]
            elif stamps[mid][0] > timestamp: 
                r = mid - 1
            else: 
                l = mid + 1
        
        # incase the key is after the timestamp
        if stamps[r][0] > timestamp: 
            return ""

        return stamps[r][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
