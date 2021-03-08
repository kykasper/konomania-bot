import random

import boto3
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

# dynamodb
TABLENAME = 'konomania-tweet'
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLENAME)

def lambda_handler(event, context):
    # dynamodbをscanし、ランダムにitem_idを作成
    count_data = table.scan(Select='COUNT')
    cnt = count_data['Count']
    item_id = random.randrange(cnt)

    #getItemメソッドの呼び出し(主キー検索)
    response = table.get_item(
        #パラメーターとして主キー情報(辞書型)を渡す
        #Keyという変数名?は固定(違う名前だとエラーになる)
        Key={
            #主キー情報を設定
            #今回はテーブルにid(プライマリーキー)・sex(ソートキー)を定義した
            'id': item_id,
        }
    )
    #結果の取得
    item = response['Item']

    #辞書型オブジェクトとして取得できる(テーブルのカラムが定義されている)
    #キーに一致するものがない場合、エラーとなる
    print(item)

    # tweet
    tweet = response['Item']["tweet"].replace('\\n', '\n')
    api.update_status(tweet)

if __name__ == "__main__":
    event = {}
    context = ""
    lambda_handler(event, context)