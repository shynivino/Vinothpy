import tweepy
'''
pip install tweepy
Setup Dev Twitter account
Create App update mobile number if it asks
Enter COnsumer key,Consumer Secrete,Access Key,Access Secrete and Twitter handle eg.. @XXXXXXXXXX
'''

 
# Fill the X's with the credentials obtained by 
# following the above mentioned procedure.
consumer_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
consumer_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
 
# Function to extract tweets
def get_tweets(username):
         
        # Authorization to consumer key and consumer secret
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 
        # Access to user's access key and access secret
        auth.set_access_token(access_key, access_secret)
 
        # Calling api
        api = tweepy.API(auth)
 
        # 200 tweets to be extracted
        number_of_tweets=200
        tweets = api.user_timeline(screen_name=username)
 
        # Empty Array
        tmp=[] 
 
        # create array of tweet information: username, 
        # tweet id, date/time, text
        tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created 
        for j in tweets_for_csv:
 
            # Appending tweets to the empty array tmp
            tmp.append(j) 
 
        # Printing the tweets
        print(tmp)
def update_tweets():
        try:
                auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
                 
                # authentication of access token and secret
                auth.set_access_token(access_key, access_secret)
                api = tweepy.API(auth)
                 
                # update the status
                api.update_status(status ="Hello Everyone, Good Night!")
                print "Updated"
        except Exception as e:
                print e
 
# Driver code
if __name__ == '__main__':
 
    # Here goes the twitter handle for the user
    # whose tweets are to be extracted.
    update_tweets()
    get_tweets("@HULUGAPPA4") 

