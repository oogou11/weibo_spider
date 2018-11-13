import logging
import scrapy
from scrapy_splash import SplashRequest
from scrapy.http import Request, FormRequest


class WeiBoSpider(scrapy.Spider):
    name = 'weibo_spider'
    allowed_domains = ["krcom.cn"]
    start_urls = [
    ]

    def start_requests(self, response):
        splash_args = {
            'wait': 0.5,
        }
        for url in self.start_urls:
            yield SplashRequest(url, self.parse_result, endpoint='render.html',
                                args=splash_args)

    def parse_result(self, response):
        logging.info(u'----------使用splash爬取京东网首页异步加载内容-----------')
        guessyou = response.xpath('//div[@id="guessyou"]/div[1]/h2/text()').extract()
        logging.info(u"find：%s" % guessyou)
        logging.info(u'---------------success----------------')



