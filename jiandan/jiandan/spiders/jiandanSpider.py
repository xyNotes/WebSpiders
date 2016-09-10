#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import scrapy
from scrapy.selector import Selector
from jiandan.items import JiandanItem

class JiandanMeizhi(scrapy.Spider):
    name = 'jiandan'
    start_urls = ['http://jandan.net/ooxx']



    def parse(self, response):
        selector = Selector(response)
        pic = selector.xpath('//a[@class="view_img_link"]/@href').extract()
        item = JiandanItem()
        item['image_urls'] = pic
        yield item

        nextHref = selector.xpath('//a[@title="Older Comments"]/@href').extract()
        if nextHref:
            nextHref=nextHref[0]
            yield scrapy.Request(nextHref,callback=self.parse)





