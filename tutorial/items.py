# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    rate = scrapy.Field()
    author = scrapy.Field()

class NovelItem(scrapy.Item):
    novel_name = scrapy.Field()
    novel_author = scrapy.Field()
    novel_title = scrapy.Field()
    novel_content = scrapy.Field()