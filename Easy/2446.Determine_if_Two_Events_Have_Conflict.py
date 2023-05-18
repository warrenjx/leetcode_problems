class Solution(object):
    def haveConflict(self, event1, event2):
        """
        :type event1: List[str]
        :type event2: List[str]
        :rtype: bool
        """
        int_event1 = []
        int_event2 = []

        # turns the events into integers to compare
        for time in event1: 
            temp = time.split(':')
            int_event1.append(int(temp[0]) * 100 + int(temp[1]))
        
        for time in event2: 
            temp = time.split(':')
            int_event2.append(int(temp[0]) * 100 + int(temp[1]))

        if (int_event1[0] < int_event2[0]): 
            if (int_event1[1] < int_event2[0]): 
                return False
        if (int_event2[0] < int_event1[0]): 
            if (int_event2[1] < int_event1[0]): 
                return False
        
        return True
