import tweepy
from tweepy import OAuthHandler
print "\n \nHey there this is my twitter-app Compe-tweet-ion which counts from 2 users who has the most words in their last 10 tweets.\n\n"

consumer_key = 'bnQBeK91BqRVEUa92xgPv1AGA'
consumer_secret = 'll2VUvXJ4WHgsENBtQ6AIHBSH4yRHDFaqbke4ZyaWP30JJ88aR'
access_token = '829056172204388352-DwCtrDVBcp9WVwFD9ab5PIhgDTDP4CV'
access_secret = 'dwX9BFnguj8KykqZ0kjVntTA2KPlVoCJxorxQkmvDieiZ'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

user1 = raw_input("\n Please give the first person's username \n")
user2 = raw_input("\nPLease give the second person's username \n")

#first user
timeline = api.user_timeline(screen_name=user1, include_rts=False, count=15000)
sum=0
sumx=""
for tweet in timeline:
        if not tweet.retweeted:

              x= " "+(tweet.text)
              sumx=sumx+x
              sum=sum+1
              if (sum==10):
                 break
lenuser1= len(sumx.split())


#second user
timeline = api.user_timeline(screen_name=user2, include_rts=False, count=15000)
sum=0
sumx=""
for tweet in timeline:
        if not tweet.retweeted:

              x= " "+(tweet.text)
              sumx=sumx+x
              sum=sum+1
              if (sum==10):
                 break
lenuser2= len(sumx.split())

if (lenuser1>lenuser2):
    print "\n\n"+user1+ " wins!!! with", (lenuser1-lenuser2)," more words in their last 10 tweets!!\n"
else:
    print "\n\n Bad luck "+ user1+" "+"it seems "+ user2 +" won with",(lenuser2-lenuser1)," more words in his/her last 10 tweets!!\n"
print "Total words in their last 10 Tweets:"
print user1 +" = ",lenuser1
print user2 +" = ",lenuser2,"\n\n"
print "Thanks for using Compe-tweet-ion !!!"
print "Made by Dionisis Nikas\n\n"
