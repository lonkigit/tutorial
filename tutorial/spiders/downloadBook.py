import scrapy

class QuotesSpider(scrapy.Spider):
    name = "xiaoshuo1"

    start_urls = [
        'http://www.bxwx9.org/b/28/28958/5509231.html',
        # 'http://www.bxwx9.org/b/28/28958/38243615.html'
    ]


    def parse(self, response):

        xiaoshuotitle = response.xpath('//meta[@name="keywords"]/@content').extract_first()
        # print('book name: %s' % xiaoshuotitle.split(" ")[0].strip())
        print('book name: %s' % xiaoshuotitle)
        self.bookname = xiaoshuotitle
        self.download(response)

        # follow pagination links
        for href in response.xpath('//ul/li[4]/a'):
            if href.xpath("@href").extract_first() == 'index.html':
                break
            yield response.follow(href, self.parse)

    def download(self,response):
        filename = '/home/lonki/pythonspider/books/%s 1.txt' % self.bookname
        with open(filename,'a+', encoding='utf-8') as file:
            # print(''.join(response.css('#content').extract_first()
            #               .replace('<div id="content"><div id="adright"></div>', '')
            #               .replace('</div>', '').split()).replace('<br>', '\n')) # 使用join去空格符号
            content = ''.join(response.xpath('//div[@id="content"]').extract_first().replace('<div id="content"><div id="adright"></div>', '')
                          .replace('</div>', '').split()).replace('<br>', '\n')
            file.write(content)
            file.write('\n')
            file.close()



