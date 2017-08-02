# -*- coding: utf-8 -*-
import scrapy
import re

from tutorial.items import TutorialItem


class DbbookSpider(scrapy.Spider):
    name = 'dbbook'
    # allowed_domains = ['https://www.douban.com/doulist/1264675/']
    start_urls = ['https://www.douban.com/doulist/1264675/']

    def parse(self, response):
        # print(response.body)
        item = TutorialItem()
        selector = scrapy.Selector(response)
        books = selector.xpath('//div[@class="bd doulist-subject"]')
        for each in books:
            title = each.xpath('div[@class="title"]/a/text()').extract()[0]
            title = title.replace(' ','').replace('\n','')
            try:
                rate = each.xpath('div[@class="rating"]/span[@class="rating_nums"]/text()').extract()[0]
            except IndexError:
                rate = 0.0
            author = re.search('<div class="abstract">(.*?)<br',each.extract(),re.S).group(1)
            author = author.replace(' ', '').replace('\n', '')
            print('标题： %s' % title)
            print('评分： %s' % rate)
            print('作者： %s' % author)
            print('')

            item['title'] = title
            item['rate'] = rate
            item['author'] = author

            yield item


        #next page
        for href in selector.xpath('//span[@class="next"]/link/@href'):
            yield response.follow(href,self.parse)
