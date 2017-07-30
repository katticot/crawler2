import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class DemoSpider(CrawlSpider):
    name = "demo"
    allowed_domains = ["www.lemonde.fr"]
    start_urls = ["http://www.lemonde.fr"]

    rules = (
        Rule(LinkExtractor(allow=(), restrict_xpaths=("//div[@class = 'next']",)),
             callback="parse_item", follow=True),
    )

    def parse_item(self, response):
        item = DemoItem()

    item["product_title"] = response.xpath("a/text()").extract()
    item["product_link"] = response.xpath("a/@href").extract()
    item["product_description"] = response.xpath("div[@class = 'desc']/text()").extract()
    return items