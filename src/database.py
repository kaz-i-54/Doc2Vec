import pandas as pd
import os

if __name__ == "__main__":
    from pymongo import MongoClient
    import sys

    if not os.path.exists('./data'):
        os.mkdir('./data')

    url = sys.argv[1]

    # MongoDBに接続し, テキストデータを取得
    client = MongoClient(url)
    collection = client['test']['hateb']

    df = pd.DataFrame.from_dict(list(collection.find())).astype(object)
    pd.DataFrame.to_csv(df, './data/hateb.csv')


# 保存したcsvファイルから文章データを取り出す
def getDocuments():
    df = pd.read_csv('./data/hateb.csv')
    df['content'] = df['content'].apply(lambda x : str(x))
    return list(df['content'])
