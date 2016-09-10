#!/usr/bin/env python3
# -*-coding: utf-8-*-

import os
import requests
from bs4 import BeautifulSoup

#创建目录
path = os.getcwd()
new_path = os.path.join(path,'韩国悬疑')
if not os.path.isdir(new_path):
    os.mkdir(new_path)


def urlopen(url):
    headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'}
    r = requests.get(url,headers = headers).text
    return r



def get_info(url,num):
    soup = BeautifulSoup(urlopen(url),'lxml')
    informations = soup.find_all('div',class_="pl2")
    for info in informations:
        name = []
        time = []
        score = []
        name.append(info.a.get_text().replace(' ', '').replace('\n', ''))
        time.append(info.p.get_text().split(r'/')[0])
        try:
            info.find(class_="rating_nums").get_text()
            score.append(info.find(class_="rating_nums").get_text())
        except AttributeError:
            score.append('None')

        with open(new_path+r'/'+'悬疑_'+str(num)+'.txt','a+') as f:
            f.write(name[0]+'  ')
            f.write(time[0]+'  ')
            f.write(score[0]+'\n'*4)


def main():
    for num in range(18):
        url = r'https://movie.douban.com/tag/韩国 悬疑?start=%s&type=T' % str(num * 20)
        get_info(url,num+1)


if __name__ == '__main__':
    main()
