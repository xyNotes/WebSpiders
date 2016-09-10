#!/usr/bin/env python3


import os, re
import requests
from lxml import etree

# 创建根目录
path = os.getcwd()
global new_path
new_path = os.path.join(path, '电影天堂种子')
if not os.path.isdir(new_path):
    os.mkdir(new_path)


# 根目录下的子目录
def mkdirs(num, title):
    global new_path
    pa = os.path.join(new_path, str(num))
    path = os.path.join(pa, str(title))
    if not os.path.isdir(pa):
        os.mkdir(pa)
    if not os.path.isdir(path):
        os.mkdir(path)
    return path



# 获取电影列表
def getUrl(url):
    mainUrl = 'http://www.bttiantang.com'

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'
    }
    req = requests.get(url, headers=headers).content
    selector = etree.HTML(req)
    movieList = selector.xpath('//p[@class="tt cl"]')
    movieHref = []
    for each in movieList:
        movieHref.append(mainUrl + each.xpath('a/@href')[0])
    return movieHref


# 获取电影链接
def getInfo(movieHref, num):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'
    }
    reqUrl = 'http://www.bttiantang.com/download4.php'
    for each in movieHref:
        response = requests.get(each, headers=headers).content
        html = etree.HTML(response)
        mulu = html.xpath('//div[@class="title"]/h2')[0]
        moviemulu = mulu.xpath('string(.)').replace(r'/', ' ')
        selector = html.xpath('//div[@class="tinfo"]')
        for each in selector:
            url = each.xpath('a/@href')[0]
            title = each.xpath('a/@title')[0]
            mytitle = title.replace(r'/', '_')
            id = re.search('id=(\d+)&', url, re.S).group(1)
            uhash = re.search('uhash=(\w+)', url, re.S).group(1)
            formData = {
            'action': 'download',
            'id': id,
            'uhash': uhash,
            'imageField.x': 62,
            'imageField.y': 33,
            }
            req = requests.post(reqUrl, headers=headers, data=formData).content
            with open(mkdirs(num, moviemulu) + r'/' + mytitle + '.torrent', 'wb') as f:
                f.write(req)


def main():
    for num in range(1, 10 + 1):
        url = 'http://www.bttiantang.com/?PageNo=%s' % num
        film = getUrl(url)
        getInfo(film, num)


if __name__ == "__main__":
    main()