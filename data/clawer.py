import requests
import json
import pandas as pd 
import random
import time

def get_data(urls_, headers_=None):
    data_ = []
    for i, (cotegory, url_) in enumerate(urls_.items(), 1):
        # 请求接口获取json数据
        res = requests.get(url_,headers=headers_)
        if res.status_code != 200: 
            ValueError(f"HTTP 请求失败，状态码为: {res.status_code}")
        # 解析并存储数据
        json_obj = json.loads(res.text)
        for item in json_obj.get("data", []):
            title = item.get('title', '')
            abstract = item.get('Abstract', '')
            if title != '' and abstract != '':
                item = (title, abstract, cotegory)
                data_.append(item)
        time.sleep(random.uniform(1, 2.5))
    return data_
urls = {
    '娱乐': 'https://www.toutiao.com/api/pc/list/feed?channel_id...', 
    '军事': 'https://www.toutiao.com/api/pc/list/feed?channel_id...',
    '财经': 'https://www.toutiao.com/api/pc/list/feed?channel_id...',
    '科技': 'https://www.toutiao.com/api/pc/list/feed?channel_id...', 
    '体育': 'https://www.toutiao.com/api/pc/list/feed?channel_id...',
    '美食': 'https://www.toutiao.com/api/pc/list/feed?channel_id...', 
    '旅游': 'https://www.toutiao.com/api/pc/list/feed?channel_id...'}
headers = {
    'User-Agent': 'Mozilla/5.0...', 
    'cookie': '...'
}
data_list = get_data(urls, headers)
res = []
for i in range(1000) :
    data_list = get_data(urls, headers)
    res.extend(data_list)
    print(f"第 {i+1} 次请求完成，获取 {len(data_list)} 条数据")

data = pd.DataFrame(res)
data.columns = ['标题', '摘要', '类别']
data = data.drop_duplicates()
data.to_csv('hot_news.csv', index=False)