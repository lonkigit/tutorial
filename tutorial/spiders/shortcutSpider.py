import scrapy


class ShortcutSpider(scrapy.Spider):
    name = "shortcutSpider"
    start_urls = [
        'http://quotes.toscrape.com/page/1/'
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text' : quote.css('span.text::text').extract_first(),
                'author' : quote.css('small.author::text').extract_first(),
                'tags' : quote.css('div.tags a.tag::text').extract(),
            }

        #1
        # next_page = response.css("li.next a::attr(href)").extract_first()
        # if next_page is not None:
        #     yield response.follow(next_page,callback=self.parse)

        #2
        # for href in response.css("li.next a::attr(href)"):
        #     yield response.follow(href,callback=self.parse)

        #3
        for a in response.css("li.next a"):
            yield response.follow(a,callback=self.parse)


