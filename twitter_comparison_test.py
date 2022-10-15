import twitter_comparison as world
from pytest import approx

def check_avg_score:
  assert world.generate_average_sentiment_score(all_tweets) == average_score;
def check_get_sentiment:
  assert world.get_sentiment(all_tweets) == sentiment_scores
def check_get_tweets:
  assert world.get_tweets(keyword) == all_tweets