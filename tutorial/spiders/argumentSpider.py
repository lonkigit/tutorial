import scrapy

class ArgumentSpider(scrapy.Spider):
    name = "argumentSpider"

    def start_requests(self):
        url = 'http://quotes.toscrape.com/'
        tag = getattr(self,'tag',None)
        if tag is not None:
            url = url + 'tag/' + tag
        yield scrapy.Request(url,self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text':quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
            }

        # for href in response.css('li.next a::attr(href)'):
        #     yield response.follow(href,self.parse)

