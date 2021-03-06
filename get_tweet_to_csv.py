import tweepy

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

# 好きな言葉をツイート
res = api.user_timeline(screen_name="CheerOnKonomin", count=100, tweet_mode='extended')

for i in res:
    print(i.full_text)
    print(i._json["entities"]["urls"])
    print(i._json["entities"]["hashtags"])

    break