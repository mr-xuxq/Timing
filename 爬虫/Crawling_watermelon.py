import requests
import json
import time
import math
import hashlib
import re
import random
from zlib import crc32
from bs4 import BeautifulSoup


# 61887739373 影视
# 6797027941 推荐
def get_url(channelId='6797027941'):
    url = 'https://www.ixigua.com/api/feedv2/feedById?&channelId={}&count=18&maxTime='.format(channelId)
    print(url)
    return url


tt_webid = ""


def get_item(url):
    headers = {
        'user-agent': "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Mobile Safari/537.36"}
    resp = requests.get(url, headers=headers, cookies='')
    wbdata = resp.content
    wbdata2 = json.loads(wbdata.decode('utf-8'))

    data1 = wbdata2['data']
    channelFeed = data1['channelFeed']
    BaseResp = channelFeed['BaseResp']
    if BaseResp['StatusMessage'] == 'error':
        return 0

    data = channelFeed['Data']
    for news in data:
        title = news['videoTitle']
        news_url = news['videoId']
        news_url = "https://www.ixigua.com/i" + news_url
        writer("bbb.txt", title, news_url)

        print(title, news_url)
        getinfo(news_url)
        time.sleep(1)
    return


# 写文件
def writer(filename, content, source='', time='', tags=''):
    write_flag = True
    with open(filename, 'a', encoding='utf-8') as f:
        f.write('内容：' + '\n')
        f.writelines(content)
        f.write('\n\n')
        f.write('作者：' + source + '\n')
        f.write('时间：' + time + '\n')
        f.write('标签：' + tags + '\n')
        f.write('------------------------分割线------------------------' + '\n\n')


def getinfo(video_id):
    return


def main(refresh=10):
    for x in range(0, refresh + 1):
        print("{0}".format(x))
        url = get_url()
        get_item(url)


if __name__ == '__main__':
    main()