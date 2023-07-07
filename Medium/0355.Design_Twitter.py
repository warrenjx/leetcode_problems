class Twitter(object):

    def __init__(self):
        # dictionary of: user_id : 10 most recent tweets
        self.users = {}
        # dictionary of: user_id: users user_id is following
        self.follows = {}
        # count for indicating the order of things arriving
        self.time = 0


    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        # format: (time, tweetId)
        if userId not in self.users: 
            self.users[userId] = [(self.time, tweetId)]
        else: 
            if len(self.users[userId]) >= 10: 
                heappushpop(self.users[userId], (self.time, tweetId))
            else: 
                heappush(self.users[userId], (self.time, tweetId))
        
        # all tweets are tied to the same timer
        self.time += 1
        

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        # raw feed contains the 10 tweets from user and followees and their timestamps
        raw_feed = []
        
        # add user's own tweets to raw feed
        if userId in self.users: 
            raw_feed += self.users[userId]

        # add user's followee's tweets to raw feed
        if userId in self.follows: 
            for user in self.follows[userId]: 
                if user in self.users: 
                    raw_feed += self.users[user]
        
        # sort raw feed by time, greatest first
        raw_feed.sort(key=lambda x:x[0], reverse=True)

        # add 10 most recent tweets to feed
        feed = []
        for i in range(min(len(raw_feed), 10)): 
            feed.append(raw_feed[i][1])

        return feed
        

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId not in self.follows: 
            self.follows[followerId] = {followeeId}
        else: 
            self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId in self.follows: 
            self.follows[followerId].remove(followeeId)
        

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
