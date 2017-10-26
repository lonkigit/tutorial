import scrapy

class QuotesSpider(scrapy.Spider):
    name = "xiaoshuo2"

    start_urls = [
        'http://www.qu.la/book/40867/2536375.html'
    ]


    def parse(self, response):

        xiaoshuotitle = response.xpath('//meta[@name="keywords"]/@content').extract_first()
        print('book name: %s' % xiaoshuotitle.split(",")[0].strip())
        # print('book name: %s' % xiaoshuotitle.split(",")[1].strip())
        self.bookname = xiaoshuotitle.split(",")[0].strip()
        self.download(response)




        #follow pagination links
        for href in response.xpath('//a[@id="A3"]'):
            if href.xpath("@href").extract_first() == './':
                break
            yield response.follow(href, self.parse)

    def download(self,response):
        filename = '/home/lonki/pythonspider/books/%s.txt' % self.bookname
        with open(filename,'a+', encoding='utf-8') as file:
            # print(''.join(response.css('#content').extract_first()
            #               .replace('<div id="content"><div id="adright"></div>', '')
            #               .replace('</div>', '').split()).replace('<br>', '\n')) # 使用join去空格符号
            content = ''.join(response.xpath('//div[@id="content"]').extract_first().replace('<div id="content"><div id="adright"></div>', '')
                          .replace('</div>', '').split()).replace('<br>', '\n').replace('<divid="content">', '').replace('<script>chaptererror();</script>','')\
                          .replace('G_罩杯女星偶像首拍A_V勇夺冠军在线观看!请关注微信公众号!:meinvlu123(长按三秒复制)!!','').replace('”#####新文，求支持哦！么么！','')\
                .replace('本站重要通知:请使用本站的免费小说APP,无广告、破防盗版、更新快,会员同步书架,请关注微信公众号 appxsyd (按住三秒复制) 下载免费阅读器!! ','')
            file.write(response.xpath('//meta[@name="keywords"]/@content').extract_first().split(",")[1].strip())
            file.write('\n')
            file.write(content)
            file.write('\n')
            file.close()



