import scrapy

from tutorial.items import NovelItem


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['www.bxwx9.org']
    # 所有分类
    start_urls = ['http://www.bxwx9.org/bsort{}/0/1.htm'.format(i) for i in range(9, 10)]  # 某个类

    def parse(self, response):
        # 所有列表页
        total = int(response.css('a[class=last]::text').extract_first())
        base_url = response.url[:-5]
        list_url = ['{}.htm'.format(i) for i in range(1, total + 1)]
        for url in list_url:
            url = base_url + url
            print(url)
            yield scrapy.Request(url=url,
                                 callback=self.novel_list_get,
                                 )

    def novel_list_get(self, response):
        # 所有小说
        for novel in response.css('table>tr'):
            novel_tag = str(novel.css('td>a[href*=binfo]::attr(href)').extract_first())[26:-4]
            novel_url = 'http://www.bxwx9.org/b{}/index.html'.format(novel_tag)
            yield scrapy.Request(url=novel_url,
                                 callback=self.novel_get,
                                 )

    def novel_get(self, response):
        # 某一本小说
        novel_name = response.css('#title::text').extract_first()
        print(novel_name)
        novel_author = response.css('#info>a[href*=author]::text').extract_first()
        print(novel_author)
        base_url = response.url[:-10]
        for dd in response.css('dl > dd'):
            next_url = dd.css('a[href*=html]::attr(href)').extract_first()
            if (next_url):
                next_url = base_url + next_url
                print(next_url)
                yield scrapy.Request(url=next_url,
                                     callback=self.save,
                                     meta={
                                         'novel_name': novel_name,
                                         'novel_author': novel_author
                                     })

    def save(self, response):
        # 某一本的某一章节
        '''''
        书名
        数字.txt
        title
        content
        :param response:
        :return:
        '''
        novel_item = NovelItem()
        novel_item['novel_name'] = response.meta['novel_name']
        novel_item['novel_author'] = response.meta['novel_author']
        novel_item['novel_title'] = response.css('#title::text').extract_first()
        novel_item['novel_content'] = ''.join(response.css('#content').extract_first(). \
                                              replace('<div id="content"><div id="adright"></div>', ''). \
                                              replace('</div>', '').split()). \
            replace('<br>', '\n')  # 使用join去空格符号
        return novel_item
