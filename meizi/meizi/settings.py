# -*- coding: utf-8 -*-

# Scrapy settings for meizi project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'meizi'

SPIDER_MODULES = ['meizi.spiders']
NEWSPIDER_MODULE = 'meizi.spiders'

ITEM_PIPELINES = {'meizi.pipelines.MeiziImagesPipeline':1,

                  }

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'

IMAGES_STORE = '/home/xnotes/meizi/meiziJanpan'



