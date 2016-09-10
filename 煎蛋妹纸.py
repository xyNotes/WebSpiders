#!/usr/bin/env python3
# -*-coding: utf-8-*-

import os,requests
import threading
import time
from bs4 import BeautifulSoup


#创建根目录
path = os.getcwd()
global new_path
new_path = os.path.join(path,'煎蛋妹纸')
if not os.path.isdir(new_path):
    os.mkdir(new_path)



#根目录下的子目录，用于存放图片
def mkdirs(num):
    global new_path
    path = os.path.join(new_path,str(num))
    if not os.path.isdir(path):
        os.mkdir(path)
    return path

#获取网页信息
def url_open(url):
    headers = {"User-Agent":"Mozilla/5. (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"}
    return requests.get(url,headers = headers).content



#图片下载函数的类
class Photo_Download_Thread(threading.Thread):
    def __init__(self, threadingsum, url,num):
        threading.Thread.__init__(self)
        self.threadingsum = threadingsum
        self.url = url
        self.num = num

    def run(self):
        with self.threadingsum:
            time.sleep(3)
            photo_url = []
            photo_name = []
            count = 0
            r = url_open(self.url)
            soup = BeautifulSoup(r,'lxml')
            img = soup.find_all('a', class_="view_img_link")
            if img:
                for i in img:
                    photo_url.append(i.get('href'))
                    photo_name.append(i.get('href').split('/')[-1])
                    with open(mkdirs(self.num) + r'/' + photo_name[count], 'wb') as file:
                        file.write(url_open(photo_url[count]))
                        count += 1
            else:
                print('网页爬虫被封了,,,')


#程序运行函数
def main():

    download = input("输入1到2055:")
    download_page = int(download)
    print("此程序功能为下载从%d到2055页面之间的煎蛋网上妹纸的图片" % download_page)
    #page = 1  # 记录下载页数
    thread_num = 10
    threadingsum = threading.Semaphore(thread_num)
    for count in range(2055, (download_page - 1), -1):
        url = 'http://jandan.net/ooxx/page-%s#comments' % count
        time.sleep(1)
        Photo_Download_Thread(threadingsum, url, count).start()
        #print('下载完成%d页妹纸' % page)
        #page += 1



if __name__ == '__main__':
    main()

