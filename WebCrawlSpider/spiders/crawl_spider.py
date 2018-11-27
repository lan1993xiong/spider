import scrapy
from scrapy.conf import settings
from scrapy import Request
from  WebCrawlSpider.items import TeacherItem
import re

class CrawlSpider(scrapy.Spider):
    name = "teacher"
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
            flag =  re.search("\【\d{4}\-\d{4}教师情况调查表\】\S+",className)
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
                item = TeacherItem()
                item['className'] =  response.meta["className"]
                temp = re.findall(r"【\S+】",con.xpath('./div[1]/dl/dd/text()').extract()[0])
                item['teacherName']= re.split("【|】",temp[0],2)[1]
                item['attendance'] = "".join(con.xpath('.//div[1]/table/tr[2]/td[2]/text()').extract()[0].split()) 
                item['knowledge']  = "".join(con.xpath('.//div[1]/table/tr[3]/td[2]/text()').extract()[0].split())
                item['patience']= "".join(con.xpath('.//div[1]/table/tr[4]/td[2]/text()').extract()[0].split())
                item['strict']= "".join(con.xpath('.//div[1]/table/tr[5]/td[2]/text()').extract()[0].split())
                item['model']= "".join(con.xpath('.//div[1]/table/tr[6]/td[2]/text()').extract()[0].split())
                item['democratic']= "".join(con.xpath('.//div[1]/table/tr[7]/td[2]/text()').extract()[0].split())
                item['task']= "".join(con.xpath('.//div[1]/table/tr[8]/td[2]/text()').extract()[0].split())
                item['method']= "".join(con.xpath('.//div[1]/table/tr[9]/td[2]/text()').extract()[0].split())
                item['progress']= "".join(con.xpath('.//div[1]/table/tr[10]/td[2]/text()').extract()[0].split())
                yield item
                
                
            
               
               