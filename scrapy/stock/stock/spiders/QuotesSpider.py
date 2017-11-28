import scrapy
from scrapy.spiders import BaseSpider, CrawlSpider
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            # 'http://quotes.toscrape.com/page/1/',
            # 'http://quotes.toscrape.com/page/2/',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=0',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=1',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=2',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=3',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=4',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=5',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=6',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=7',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=8',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=9',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=10',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=11',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=12',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=13',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=14',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=15',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=16',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=17',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=18',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=19',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=20',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=21',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=22',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=23',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=24',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=25',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=26',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=27',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=28',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=29',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=30',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=31',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=32',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=33',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=34',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=35',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=36',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=37',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=38',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=39',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=40',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=41',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=42',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=43',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=44',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=45',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=46',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=47',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=48',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=49',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=50',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=51',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=52',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=53',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=54',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=55',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=56',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=57',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=58',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=59',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=60',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=61',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=62',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=63',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=64',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=65',
            'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=66',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)
        page = Selector(response)
        # stock_name = page.xpath('//*[@id="CompanylistResults"]/tbody/tr[1]/td[2]/h3')
        test = page.xpath('//h3//a/text()')

        index = response.url.split('=')[-1]
        stock_list = test.extract()
        stock_str = ''
        for sto in stock_list[:-1]:
            # print sto
            stock_str += sto.strip() + "+"
        stock_str += stock_list[-1].strip()

        with open('stock_list_' + index, 'wb') as f:
            f.write(stock_str)
        # self.log('Saved file %s' % filename)
