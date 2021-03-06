import pandas as pd
import numpy as np

csv_path = "./tweets.csv"
save_path = "./fixed_tweets.csv"

df = pd.read_csv(csv_path, header=None)
df = df[~df[0].str.contains('#はてなブログ')]
df = df[~df[0].str.contains('www.youtube.com/playlist')]
df[0] = df[0].mask(~df[0].str.contains('anime.dmkt-sp.jp'), df[0].str.replace('#鈴木このみ', ''))
array = df[0].unique()
array = np.sort(array)
pd.DataFrame(array).to_csv(save_path, header=False, index=False, encoding="utf-8")
