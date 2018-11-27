import scrapy
from scrapy.conf import settings
from scrapy import Request
from  WebCrawlSpider.items import SurveyItem
import re

class CrawlSpider(scrapy.Spider):
    name = "survey"
    allowed_domains = ["wjx.cn"]
    start_urls = [
        "https://www.wjx.cn/newwjx/manage/myquestionnaires.aspx"
    ] 
    url="https://www.wjx.cn"
    headers = {
        'Connection': 'keep - alive',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
    }
    meta = {
        'dont_redirect': True,  # 禁止网页重定向
        'handle_httpstatus_list': [301, 302]  # 对哪些异常返回进行处理
    }
    cookie = settings['COOKIE']
     
    def start_requests(self):
          yield Request(self.start_urls[0], callback=self.parse, cookies=self.cookie,
                      headers=self.headers, meta=self.meta)
                      
    
    def parse(self, response):
        num = 1;
        while (num <= 50):
              yield Request(self.start_urls[0]+'?pageindex='+str(num), callback=self.parseData, cookies=self.cookie,headers=self.headers, meta=self.meta)
              num = num + 1
                    
    def parseData(self,response):
        contrain = response.xpath('.//*[@id="ctl01_ContentPlaceHolder1_qls"]/dl[@class="survey-items"]')
        for con in contrain:
             item = SurveyItem();
             item['sid'] = con.xpath('.//dt[1]/div[1]/div/text()').extract()[0]
             item['cname'] = con.xpath('.//dt[1]/div[1]/a[1]/text()').extract()[0]
             item['surveynum'] = con.xpath('.//dt[1]/div[2]/div[2]/a/text()').extract()[0]
             yield item