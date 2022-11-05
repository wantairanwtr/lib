import requests
import json
import time
import random
import pandas as pd

pd.set_option('display.max_rows', None)
k_type="D1"# W1   D1   H1、H4、H12   M5、M15
url=r"https://api.libswap.com/api/bars/list?pair={}&frame={}"
lib="0x41770869bC322abc982fABb4c13FE34674e5162A"
yzz="0xA1E8Ad6E8b47D813093283029FCD15C4f83E8650"
url1=url.format(lib,k_type)
url2=url.format(yzz,k_type)
# print(url1)
# print(url2)
def requestslib(url,max_try_num=5,sleep_time=random.randint(0,5)):
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35"}
    response=requests.get(url,headers=headers,timeout=sleep_time)
    for i in range(max_try_num):
        if response.status_code==200:
            return response.text
        else:
            print("连接失败",response)
            time.sleep(sleep_time)
content=requestslib(url1)
content=json.loads(content)
k_data=content["rows"]
df=pd.DataFrame(k_data)
# print(df)
# exit()
df["time"]=pd.to_datetime(df["time"].astype(float)/1000,unit="s")+pd.Timedelta(hours=8)
print(df)