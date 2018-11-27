import scrapy
from scrapy.conf import settings
from scrapy import Request
from  WebCrawlSpider.items import punishmentItem
import re

class CrawlSpider(scrapy.Spider):
    name = "punish"
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
              yield Request(self.start_urls[0]+'?pageindex='+str(num), callback=self.parseUrl, cookies=self.cookie,headers=self.headers, meta=self.meta)
              num = num + 1
    
    def parseUrl(self, response):
        UrlContrain = response.xpath(".//*[@id='ctl01_ContentPlaceHolder1_qls']/dl[@class='survey-items']")
        for con in UrlContrain:
            className = con.xpath('.//dt[1]/div[1]/a[1]/text()').extract()[0]
            flag =  re.search("【\s*\d{4}\-\d{4}\s*有无体罚或变相体罚学生的情况调查\】",className)
            if flag!= None:
                className = re.split("】",className,1)[1]
                end_urls = con.xpath('.//dd[@class="item-bot"]/div[1]/dl[3]/dd/a/@href').extract()
                for end_url in end_urls:
                   yield Request(self.url+str(end_url), callback=self.parseData, cookies=self.cookie,headers=self.headers,meta =
                   {'className':className})      
            else:
                pass
                   
    def parseData(self,response):
            DataContrain  = response.xpath(".//*[@id='ctl02_ContentPlaceHolder1_divStatData']/div[@class='title-item']")
            for con  in DataContrain:
                item = punishmentItem()
                item['className'] =  response.meta["className"]
                temp = re.findall(r"【\S+】",con.xpath('./div[1]/dl/dd/text()').extract()[0])
                item['teacherName']= re.split("【|】",temp[0],2)[1]
                item['modelRight'] = re.split(r"\(","".join(con.xpath('.//tr[2]/td[2]/text()').extract()[0].split()),2)[0]   
                item['modelNo']  = re.split(r"\(","".join(con.xpath('.//tr[2]/td[3]/text()').extract()[0].split()),2)[0]   
                item['respectRight']= re.split(r"\(","".join(con.xpath('.//tr[3]/td[2]/text()').extract()[0].split()),2)[0] 
                item['respectNo']= re.split(r"\(","".join(con.xpath('.//tr[3]/td[3]/text()').extract()[0].split()),2)[0]
                item['insultRight']= re.split(r"\(","".join(con.xpath('.//tr[4]/td[2]/text()').extract()[0].split()),2)[0]
                item['insultNo']= re.split(r"\(","".join(con.xpath('.//tr[4]/td[3]/text()').extract()[0].split()),2)[0]
                item['hitRight']= re.split(r"\(","".join(con.xpath('.//tr[5]/td[2]/text()').extract()[0].split()),2)[0]
                item['hitNo']= re.split(r"\(","".join(con.xpath('.//tr[5]/td[3]/text()').extract()[0].split()),2)[0]
                item['punishRight']= re.split(r"\(","".join(con.xpath('.//tr[6]/td[2]/text()').extract()[0].split()),2)[0]
                item['punishNo']= re.split(r"\(","".join(con.xpath('.//tr[6]/td[3]/text()').extract()[0].split()),2)[0]
                yield item