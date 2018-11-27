# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
from WebCrawlSpider.dbhelper import DBHelper
sys.path.append('D:\WebCrawlSpider\WebCrawlSpider\pipelines.py')

from WebCrawlSpider.items import SurveyItem
from WebCrawlSpider.items import TeacherItem
from WebCrawlSpider.items import punishmentItem

class SurveyItemPipeline(object):
     
    def __init__(self):
        self.db = DBHelper()

    def process_item(self, item, spider):
        # 插入数据库
        if isinstance(item, SurveyItem): 
            self.db._insert_survey(item);
        return item




class TeacherItemPipeline(object):
     
    def __init__(self):
        self.db = DBHelper()

    def process_item(self, item, spider):
        # 插入数据库
         if isinstance(item, TeacherItem): 
             self.db._insert_teacher(item);
         return item

class punishmentItemPipeline(object):
     
    def __init__(self):
        self.db = DBHelper()

    def process_item(self, item, spider):
        # 插入数据库
         if isinstance(item, punishmentItem): 
             self.db._insert_punish(item);
         return item


   

  