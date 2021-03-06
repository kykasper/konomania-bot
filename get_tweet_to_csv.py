
import pandas as pd
import tweepy

import config
import twitter_config

# 先ほど取得した各種キーを代入する
CK=twitter_config.CONSUMER_KEY
CS=twitter_config.CONSUMER_SECRET
AT=twitter_config.ACCESS_TOKEN
AS=twitter_config.ACCESS_TOKEN_SECRET

# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
api = tweepy.API(auth)



def replace_urls(text, urls):
    urls.sort(key=lambda url: url["indices"][0])
    for url in sorted(urls, key=lambda url: url["indices"][0], reverse=True):
        x, y = url["indices"]
        text = text[:x] + url["expanded_url"] + text[y:]
    return text

def get_tweet_list(screen_name):
    tweet_list = []
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=screen_name, count=100, tweet_mode='extended', wait_on_rate_limit = True).items():
        full_text = tweet.full_text
        text = replace_urls(full_text, tweet.entities["urls"])
        text = '\\n'.join(text.splitlines())
        tweet_list.append([text])
    return tweet_list

def main():
    screen_name = "CheerOnKonomin"
    save_path = "./tweets.csv"
    tweet_list = get_tweet_list(screen_name)
    pd.DataFrame(tweet_list).to_csv(save_path, header=False, index=False, encoding="utf-8")
    
if __name__ == "__main__":
    main()