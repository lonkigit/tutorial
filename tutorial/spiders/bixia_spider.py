import scrapy

class BixiaSpider(scrapy.Spider):
    name = 'bixiaspider'
    start_urls = [
       'http://www.bxwx9.org/btopallvisit/0/1.htm'
    ]


    def parse(self, response):
        table = response.css('table.grid')
        books = table.css('td.odd')
        page = 1
        for book in books.css('td.odd::text').extract():
            yield {
                'book': book
            }
            page = page + 1

            if page <= 100:
                next_page = "http://www.bxwx9.org/btopallvisit/0/%d.htm" % page
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page,callback=self.parse)



