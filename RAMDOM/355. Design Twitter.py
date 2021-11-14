from collections import defaultdict

class Twitter(object):

    def __init__(self):
        self.flag = 0
        self.tweetsdict = defaultdict(list)
        self.followdict = defaultdict(list)

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.flag = self.flag+1
        self.tweetsdict[userId].append([tweetId,self.flag])
        print(self.tweetsdict)
        return None

        

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        if not userId in self.followdict[userId]:
            self.followdict[userId].append(userId)

        followlist = self.followdict[userId]
        print("followlist",followlist)
        posts = list()
        for followee in followlist:
            for eachtweet in self.tweetsdict[followee]:
                posts.append(eachtweet)
        posts.sort(key=lambda x:x[1],reverse=True)  
        return [posts[i][0] for i in range(0,10)] if len(posts)>=10 else [post[0] for post in posts]
        

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if not followeeId in self.followdict[followerId]:
            self.followdict[followerId].append(followeeId)
            print(self.followdict)
        else:
            print("Repeat")
        return None

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId in self.followdict[followerId]:
            self.followdict[followerId].remove(followeeId)
            print(self.followdict)
        else:
            print("Not found")
        return None

        

if __name__=="__main__":
    # Your Twitter object will be instantiated and called as such:
    obj = Twitter()
    obj.postTweet(1,5)
    print(obj.getNewsFeed(1))
    obj.follow(1,2)
    obj.postTweet(2, 6)
    obj.follow(1,2)
    print(obj.getNewsFeed(1))
    obj.unfollow(1,2)
    obj.unfollow(1,2)
    print(obj.getNewsFeed(1))
    obj.postTweet(1,9)
    obj.follow(1,2)
    print(obj.getNewsFeed(1))