import requests        #导入requests包
import json

def getCase():
    url = 'http://www.cntour.cn/'
    strhtml = requests.get(url)        #Get方式获取网页数据
    print(strhtml.text)

def postCase(word=None):
    url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'
    From_data = {'from': 'zh','to': 'en','query': word,
        'transtype': 'translang',
        'simple_means_flag': '3',
        'sign': '498481.227328',
        'token': 'f76e18593deb16ae95f3a9ef20d0b348',
        'domain': 'common'}
    response = requests.post(url, data=From_data)
    content = json.loads(response.text)
    print(content)
    #百度设定了反爬机制，比较攻破【sign每次都不一样】
    #打印翻译后的数据
    #print(content['translateResult'][0][0]['tgt'])

if __name__ == '__main__':
    postCase('我爱中国')
    #getCase()