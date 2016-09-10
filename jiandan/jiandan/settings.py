# -*- coding: utf-8 -*-

# Scrapy settings for jiandan project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html


BOT_NAME='jiandan'

SPIDER_MODULES=['jiandan.spiders']

NEWSPIDER_MODULE='jiandan.spiders'

ITEM_PIPELINES = {'jiandan.pipelines.MyImagesPipeline':1,

                  }

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'random_useragent.RandomUserAgentMiddleware': 400
}

USER_AGENT_LIST = "/home/xnotes/jiandan/useragents.txt"

IMAGES_STORE='/home/xnotes/meizhi'

