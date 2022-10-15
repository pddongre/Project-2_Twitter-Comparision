import tweepy
from textblob import TextBlob
import preprocessor as p
import statistics
from typing import List


with open("CK.txt") as f:
   consumer_key = f.read()

with open("CS.txt") as f:
   consumer_secret = f.read()

#consumer_key = ""
#consumer_secret = ""
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)


#Function Definitions 
def get_tweets(keyword:str)->List[str]: #function to get tweets 
    all_tweets = []
    for tweet in tweepy.Cursor(api.search_tweets, q=keyword, tweet_mode='extended',lang='en').items(10): #10 tweets
        all_tweets.append(tweet.full_text)
    return all_tweets


def clean_tweets(all_tweets: List[str])->List[str]: #clean the tweets once I get them 
    tweets_clean = []
    for tweet in all_tweets:
        tweets_clean.append(p.clean(tweet))
    return tweets_clean   

def get_sentiment(all_tweets: List[str]) -> List[float]: #gets sentiment score for each of the 10 tweets
    sentiment_scores=[]
    for tweet in all_tweets:
        blob = TextBlob(tweet)
        sentiment_scores.append(blob.sentiment.polarity)
    return sentiment_scores

def generate_average_sentiment_score(keyword: str)->int:  #generates average sentiment score for all the 10 tweets
    tweets = get_tweets(keyword)
    tweets_clean = clean_tweets(tweets)
    sentiment_scores = get_sentiment(tweets_clean)

    average_score = statistics.mean(sentiment_scores)
    return average_score


# Main 
if __name__ == "__main__":
    #api = tweepy.API(auth)
    print("Does the world prefer")
    first_thing = input()
    print("...or...")
    second_thing = input()
    print("\n")

    first_score = generate_average_sentiment_score(first_thing)
    second_score = generate_average_sentiment_score(second_thing)

    if(first_score>second_score):
        print(f"{first_thing} is more popular over {second_thing}")
    else:
        print(f"{second_thing} is more popular over {first_thing}") 