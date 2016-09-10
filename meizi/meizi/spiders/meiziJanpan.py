#!/usr/bin/env python3


import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
from meizi.items import MeiziItem


class meiziJanpan(scrapy.Spider):

    name = 'meizijanpan'

    start_urls = ['http://www.mzitu.com/japan']

    def parse(self, response):
        selector = Selector(response)
        urls = selector.xpath('//div[@class="postlist"]/ul[@id="pins"]/li/a/@href').extract()
        for url in urls:
            yield Request(url,callback=self.parse_item)

        nextPage = selector.xpath('//a[@class="next page-numbers"]/@href').extract()
        if nextPage:
            nextPage=nextPage[0]
            yield Request(nextPage,callback=self.parse)


    def parse_item(self,response):
        selector = Selector(response)
        urls = selector.xpath('//div[@class="main-image"]/p/a/img/@src').extract()[0]
        item = MeiziItem()
        item['image_urls'] = urls
        yield item


        nextPage = selector.xpath('//div[@class="pagenavi"]/a/@href').extract()
        if nextPage:
            nextPage = nextPage[-1]
            yield Request(nextPage,callback=self.parse_item)




