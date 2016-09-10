#-*- coding:utf-8 -*-

from scrapy.spiders import CrawlSpider
from scrapy.http import Request
from AiqiyiLaojiumen.items import Laojiumen
import json

class LaojiumenSpider(CrawlSpider):
    name = 'laojiumen'
    redis_key = 'laojiumen:start_urls'
    #start_urls = ['http://api.t.iqiyi.com/qx_api/comment/review/get_review_list?aid=11442675&page=1&sort=hot']
    def start_requests(self):
        for i in range(1,68+1):
            yield Request('http://api.t.iqiyi.com/qx_api/comment/review/get_review_list?aid=11442675&page=%s&sort=hot' % i)


    def parse(self, response):
        content = json.loads(response.body.decode('utf-8'))
        jsData = content['data']['reviewList']
        for each in jsData:
            item = Laojiumen()
            item['commentName'] = each['userInfo']['uname']
            item['commentTitle'] = each['title']
            item['commentView'] = each['content']
            item['commentScore'] = each['score']

            yield item

