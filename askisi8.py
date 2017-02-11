import tweepy
import time



from tweepy import OAuthHandler
print "\n \nHey there this is my twitter-app Follow-too which finds common followers from 2 users.\n\n"
print "\n WARNING!! If one of the persons has more than 150 followers it will take more time due to API limit rate !!!"
print "\n WARNING!! If one of the persons has a protected account the app won't work !!!"
consumer_key = 'DIUovDC8IpvapDORgLloQLaVJ'
consumer_secret = '1iKRar58RcFAOyaEY3p8cFEPM1st86mvbo93ZzOeYU4MYSipoE'
access_token = '829056172204388352-xoGJXYxmeUNk3jGFjBqMlOFf0ksbrRB'
access_secret = 'uONeBcwUvGfQLjU8jv3Snt96yasX6lwfyGgfvfg1DXBIx'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)
user="BasitFatima"
user2="ambermunda"
#user1 = raw_input("Please give the first person's username \n")
#user2 = raw_input("\nPLease give the second person's username \n")
print "\nPlease wait. This might take a while...\n\n"

sumx=""
for user in tweepy.Cursor(api.followers, screen_name=user).items():
   x= user.screen_name
   sumx=sumx+" "+ x
followers1=sumx.split()

sumy=""
for user in tweepy.Cursor(api.followers, screen_name=user2).items():
   x= user.screen_name
   sumy=sumy+" "+ x
followers2=sumy.split()
i=0
j=0
sum=0
l1=int(len(followers1))
l2=int(len(followers2))
followers=""
if l1>l2:
    for f1 in followers1:
        for f2 in followers2:
            if f1==f2:
                sum=sum+1
                followers=followers+" \n"+f1
else:
    for f2 in followers2:
        for f1 in followers1:
            if f1==f2:
                sum=sum+1
                followers=followers+" \n"+f1
if followers=="":
    print "Sorry no common followers found...."
else:
    print "There were ", sum, " common followers found:\n"
    print followers
    print "\n Thanks for using Follow-too"
    print "Made by Dionisis Nikas\n\n"
