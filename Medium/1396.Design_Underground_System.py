class UndergroundSystem(object):

    def __init__(self):
        self.customers = dict() # customer id : time checked in
        self.routes = dict() # start->end : (total time, total count)

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        # add customer id to customers hashtable
        self.customers[id] = (stationName, t)
        

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        if id in self.customers: 
            # need to pop, or else it messes things up
            start_station, start_t = self.customers.pop(id)

            key = start_station + "->" + stationName

            # calculate the total time and number of trips taken per route
            if key in self.routes:
                self.routes[start_station + "->" + stationName][0] += t - start_t
                self.routes[start_station + "->" + stationName][1] += 1
            else: 
                self.routes[start_station + "->" + stationName] = [t - start_t, 1]
        

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """

        # calculate average from total time spent on route and total count
        key = startStation + "->" + endStation
        if key in self.routes: 
            total_time, total_ct = self.routes[key]

            return float(total_time) / total_ct
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
