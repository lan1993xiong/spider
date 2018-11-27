# -*- coding: utf-8 -*-

# Scrapy settings for WebCrawlSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'WebCrawlSpider'

SPIDER_MODULES = ['WebCrawlSpider.spiders']

#每三秒请求一次
DOWNLOAD_DELAY = 3

#数据库配置

MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'python'         #数据库名字，请修改
MYSQL_USER = 'root'             #数据库账号，请修改
MYSQL_PASSWD = 'lan123'         #数据库密码，请修改
MYSQL_PORT = 3306               #数据库端口，在dbhelper中使用

# 设置请求头部，添加url
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    "User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;",
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,*',
    
}
REDIRECT_ENABLED = False                       # 关掉重定向, 不会重定向到新的地址
HTTPERROR_ALLOWED_CODES = [301, 302,404]     # 返回301, 302时, 按正常返回对待, 可以正常写入
# 设置item——pipelines
ITEM_PIPELINES = {

    'WebCrawlSpider.pipelines.SurveyItemPipeline':900,
    'WebCrawlSpider.pipelines.TeacherItemPipeline':990,
    'WebCrawlSpider.pipelines.punishmentItemPipeline':1000
}
COOKIE ={'Cookie:acw_tc': '2f624a7515417481353322827e0e6e94356a8e379c805879b6e5410ad74e51', 
'.ASPXANONYMOUS': 'QgdLx46u1AEkAAAAZDQxMmU2ZWYtNGU1NC00YWQ2LTlhYzUtYWFhODQ4YWNhMzFhllQf2IlaO0TRNIg081s8mNToHf01', 'WjxUser': 'UserName', 'UM_distinctid': '166f75990786f-05ee501c653b4e-b79183d-100200-166f759907bd6', 'baidutgkey': '%u95EE%u5377%u661FBH%7C2%7Cbaidu',
 'mobileuser': '13602565101', 'mqcount': '4', 'spiderregkey': 'baidu.com%c2%a7%e7%9b%b4%e8%be%be%c2%a71', 
 '_cnzz_CV4478442': '%E7%94%A8%E6%88%B7%E7%89%88%E6%9C%AC%7C%E4%BC%81%E4%B8%9A%E7%89%88%7C1543201343943', 'CNZZDATA4478442': 'cnzz_eid%3D2031174633-1541745833-https%253A%252F%252Fwww.wjx.cn%252F%26ntime%3D1543228158', 'Hm_lvt_21be24c80829bd7a683b2c536fcf520b': '1543158466,1543194802,1543200919,1543228527', 'Hm_lpvt_21be24c80829bd7a683b2c536fcf520b': '1543228527', 
 'SojumpSurvey': '010220D8DBE88A53D608FE2078ED6FAC53D608001A4B623A672875376231006D007500750069006B0065007A007A00750079007400760032006F00320072006600310072006300610000012F00FF8A88DFDB85FD82C8A934945E34A2DC356375D130', 'logcook': '1'}



# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'WebCrawlSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
REDIRECT_ENABLED = False



#####################################################
COMMANDS_MODULE = 'WebCrawlSpider.commands'
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'WebCrawlSpider.middlewares.WebcrawlspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'WebCrawlSpider.middlewares.WebcrawlspiderDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'WebCrawlSpider.pipelines.WebcrawlspiderPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
