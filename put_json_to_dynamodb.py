import json
import codecs

import pandas as pd
import boto3

csv_path = "./fixed_tweets.csv"
save_path = "./fixed_tweets.json"

df = pd.read_csv(csv_path, header=None, encoding = "utf-8")
df.columns =["tweet"]
df_json = df.to_dict(orient='records')

resource = boto3.resource('dynamodb', region_name='ap-northeast-1')

# Connect to the DynamoDB table

table = resource.Table('konomania-tweet')

# Load the JSON object created in the step 3 using put_item method

for i, tweet in enumerate(df_json):
    if i > 1: break
    tweet["id"] = i
    table.put_item(Item=tweet)


# Test
# response = table.get_item(Key={'seat_no': 'A 314216'})
# response