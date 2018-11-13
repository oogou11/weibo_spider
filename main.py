from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from weibo_spider.spiders.weibo_spider import WeiBoSpider


if __name__=='__main__':
    process = CrawlerProcess(get_project_settings())
    process.crawl('weibo_spider')
    process.start()
