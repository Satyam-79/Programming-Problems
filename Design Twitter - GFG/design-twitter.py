#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
import collections, heapq

class Twitter:
    # Compose a new tweet
    def __init__(self):
        self.followMap = collections.defaultdict(set)
        self.postMap = collections.defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.postMap[userId].append([self.count, tweetId])
        self.count-=1 #Just for creating the max-heap 

    def getNewsFeed(self, userId: int):
        res = []
        heap = []
        self.followMap[userId].add(userId)
        for user in self.followMap[userId]:
            for post in self.postMap[user][::-1]:
                heap.append(post)
        heapq.heapify(heap)
        while heap and len(res)<10:
            count, tweet = heapq.heappop(heap)
            res.append(tweet)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        # Code here

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    obj = Twitter()
    totalQueries = int(input ())
    for _ in range (totalQueries):
        query = list(map(int, input().split()))
        if (query[0] == 1):
            userId, tweetId = query[1], query[2]
            obj.postTweet(userId, tweetId)
        elif (query[0] == 2):
            userId =  query[1]
            vec = obj.getNewsFeed(userId)
            for val in vec:
                print(val, end = ' ')
            print()
        elif (query[0] == 3):
            follower, followee = query[1], query[2]
            obj.follow(follower, followee)
        else:
            follower, followee = query[1], query[2]
            obj.unfollow(follower, followee)
# } Driver Code Ends