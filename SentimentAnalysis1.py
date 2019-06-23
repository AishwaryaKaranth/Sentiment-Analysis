import re 
import tweepy 
from tweepy import OAuthHandler 
from textblob import TextBlob 
import matplotlib.pyplot as plt
'''import wordcloud
from wordcloud import WordCloud, STOPWORDS
stopwords=set(STOPWORDS)
def show_wordcloud(data, title=None):
    wordcloud=WordCloud(
        background_color='White',
        stopwords=stopwords,
        max_words= 200,
        max_font_size=40,
        scale=3,
        random_state=1 ).generate(str(data))
    fig=plt.figure(1, figsize=(12, 12))
    plt.axis('off')
    if title:
        fig.suptitle(title, fontsize=20)
        fig.subplots_adjust(top=2.3)

        plt.imshow(wordcloud)
        plt.show()'''
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
stopwords = set(STOPWORDS)
stopwords.add("TextBlob")
stopwords.add("RT")
stopwords.add("https")
stopwords.add("co")

b=[] #it is a list containing analysis
def show_wordcloud(tweets, title= None):
    wordcloud = WordCloud(
        background_color='white',
        stopwords=stopwords,
        max_words=200,
        max_font_size=40, 
        scale=3,
        random_state=1 # chosen at random by flipping a coin; it was heads
    ).generate(str(tweets))

    fig = plt.figure(1, figsize=(12, 12))
    plt.axis('off')
    if title: 
        fig.suptitle(title, fontsize=20)
        fig.subplots_adjust(top=2.3)

    plt.imshow(wordcloud)
    plt.show()
#data=['bad','good','BADD','worse']
#show_wordcloud(tweets)


  
class TwitterClient(object): 
    
   # if __name__ == "__main__": 
    # calling main function 
    #main() 

    def __init__(self): 
        
        # keys and tokens from the Twitter Dev Console 
        consumer_key = ''
        consumer_secret = ''
        access_token = ''
        access_token_secret = ''#insert the credentials obtained from twitter dev account here.
  
        # attempt authentication 
        try: 
            # create OAuthHandler object 
            self.auth = OAuthHandler(consumer_key, consumer_secret) 
            # set access token and secret 
            self.auth.set_access_token(access_token, access_token_secret) 
            # create tweepy API object to fetch tweets 
            self.api = tweepy.API(self.auth) 
           
        except: 
            print("Error: Authentication Failed") 
  
    def clean_tweet(self, tweet): 
        
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) ", " ", tweet).split()) 
 

    def get_tweet_sentiment(self, tweet): 
       
        # create TextBlob object of passed tweet text 
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment 
        if analysis.sentiment.polarity > 0: 
            b.append((analysis))
            #print(analysis)
            return 'positive' 

        elif analysis.sentiment.polarity == 0: 
            #b.append(analysis)
            return 'neutral'

        else:
            b.append(analysis) 
            return 'negative'
  
    def get_tweets(self, query, count = 100): 
       
        # empty list to store parsed tweets 
        tweets = [] 
      #  print (tweets)
        try: 
            # call twitter api to fetch tweets 
            fetched_tweets = self.api.search(q = query, count = count) 
  
            # parsing tweets one by one 
            for tweet in fetched_tweets: 
                # empty dictionary to store required params of a tweet 
                parsed_tweet = {} 
  
                # saving text of tweet 
                parsed_tweet['text'] = tweet.text 
                # saving sentiment of tweet 
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text) 
  
                # appending parsed tweet to tweets list 
                if tweet.retweet_count > 0: 
                    # if tweet has retweets, ensure that it is appended only once 
                    if parsed_tweet not in tweets: 
                        tweets.append(parsed_tweet) 
                else: 
                    tweets.append(parsed_tweet) #parsed_tweet dictionary is being appended to a list.
            #show_wordcloud(tweets)

            # return parsed tweets 
            return tweets 
  
        except tweepy.TweepError as e: 
            # print error (if any) 
            print("Error : " + str(e)) 
    #show_wordcloud(tweets)

#show_wordcloud(tweets)


  
def main(): 
    # creating object of TwitterClient Class 
    api = TwitterClient() 
    # calling function  get_tweets to get tweets
    tweets = api.get_tweets(query = "demonetisation", count = 600) #tweets is a list containing a dictionary.
    positive_tweets=[]
    negative_tweets=[]
    # picking positive tweets from tweets 
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive'] 
    # percentage of positive tweets 
    print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets))) 
    #ptweets_percentage = 100*len(ptweets)/len(tweets)
    # picking negative tweets from tweets 
    #show_wordcloud(tweets)
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative'] 
    # percentage of negative tweets 
    print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets))) 
    # percentage of neutral tweets 
    print("Neutral tweets percentage: {} %".format(100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets))) 
    #print(b)
    #show_wordcloud(b)
     #printing first 5 positive tweets 
    print("\n\nPositive tweets:") 
    for tweet in ptweets[:10]: 
    #for tweet in positive_tweets[:10]:
        print(tweet['text']) 
  
    #printing first 5 negative tweets 
    print("\n\nNegative tweets:") 
    for tweet in ntweets[:10]: 
    #for tweet in negative_tweets[:10]:
        print(tweet['text']) 
    show_wordcloud(b)
   # positive_tweets=[]
    '''for tweet in tweets:
        if tweet['sentiment']== 'positive':
        #if analysis.sentiment.polarity>0:
            positive_tweets.append(tweet)
        
    percentage_of_positive_tweets=(len(positive_tweets)/len(tweets))*100
    print("positive tweets percentage:{} %",percentage_of_positive_tweets)
   # negative_tweets = []
    for tweet in tweets:
        if tweet['sentiment']=='negative':
        #if analysis.sentiment.polarity<0:
            negative_tweets.append(tweet)

    percentage_of_negative_tweets=(len(negative_tweets)/len(tweets))*100
    print("negative tweets percentage:{} %",percentage_of_negative_tweets)''' #does not work :/
    #show_wordcloud(b)
    import plotly.plotly as py
    import plotly.tools as tools
    import matplotlib.pyplot as plt

    ptweets_percentage= 100*len(ptweets)/len(tweets)
    print(ptweets_percentage)
    ntweets_percentage= 100*len(ntweets)/len(tweets)
    print(ntweets_percentage)
    neutral_percentage= 100*((len(tweets)-len(ptweets)-len(ntweets))/len(tweets))

    y=[ptweets_percentage, ntweets_percentage, neutral_percentage]
    a=len(y)
    x=range(a)
    width = 1/2.0
    #plt.bar(x, y, width, color="blue")
    fig, xy = plt.subplots()

    x1=[1]
    y1=[ptweets_percentage]
    x2=[2]
    y2=[ntweets_percentage]
    x3=[3]
    y3=[neutral_percentage]
    plt.bar(x1, y1, width, label="Positive Tweets", color="#A61646")
    plt.bar(x2, y2, width, label="Negative Tweets", color="#4D362E")
    plt.bar(x3, y3, width, label="Neutral Tweets", color="#3C8C3F")
    plt.legend()
    plt.show()

    import matplotlib.pyplot as plt
    y=[ptweets_percentage, ntweets_percentage, neutral_percentage]
    a=len(y)
    x=range(a)
    width=1/2.0
    fig, xy = plt.subplots()
    plt.scatter(x, y, width, color="#A61646")
    plt.legend()
    plt.show()

    '''print("\n\nPositive tweets:") 
    #for tweet in ptweets[:10]: 
    for tweet in positive_tweets[:10]:
        print(tweet['text']) 
  
    #printing first 5 negative tweets 
    print("\n\nNegative tweets:") 
   # for tweet in ntweets[:10]: 
    for tweet in negative_tweets[:10]:
        print(tweet['text'])'''
    #print(b)

if __name__ == "__main__": 
    # calling main function 
    main() 
   

#if __name__ == "__main__": 
    # calling main function 
# main() 
'''import numpy as np
import matplotlib.pyplot as plt
plt.axis([0, 10, 0, 100])    # ----means xmin=0,xmax=10,ymin=0,ymax=1
for i in range(200):
    y = np.random.random()
    plt.scatter(i, y)
    plt.pause(0.5)     # It seems that after turning on interactive mode through plt.ion(), pyplot needs to be paused
                        # temporarily for it to update/redraw itself through plt.pause(0.05)
plt.show()'''
'''import plotly.plotly as py
import plotly.tools as tools
import matplotlib.pyplot as plt

ptweets_percentage= 100*len(ptweets)/len(tweets)
#print(ptweets_percentage)
ntweets_percentage= 100*len(ntweets)/len(tweets)
#print(ntweets_percentage)

y=[ptweets_percentage, ntweets_percentage]
a=len(y)
x=range(a)
width = 1/2.0
plt.bar(x, y, width, color="blue")
fig, xy = plt.subplots()

x1=[1]
y1=[ptweets_percentage]
x2=[2]
y2=[ntweets_percentage]
plt.bar(x1, y1, width, label="Positive Tweets", color="blue")
plt.bar(x2, y2, width, label="Negative Tweets", color="red")
plt.legend()
plt.show()'''
