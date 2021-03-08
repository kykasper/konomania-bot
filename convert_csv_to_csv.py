import json
import codecs

import pandas as pd
import numpy as np

csv_path = "./fixed_tweets.csv"
save_path = "./fixed_tweets.json"

df = pd.read_csv(csv_path, header=None, encoding = "utf-8")
df.columns =["tweet"]
df_json = {"konomania-tweets" : df.to_dict(orient='records')} 
# text = json.dumps(df_json, sort_keys=True, indent=4, ensure_ascii=False)
#print(text.encode("utf-8"))
with codecs.open(save_path, 'w', 'utf-8') as f:
    json.dump(df_json, f, indent=4, ensure_ascii=False)
