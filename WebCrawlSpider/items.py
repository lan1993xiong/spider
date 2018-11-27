# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import  sys


class SurveyItem(scrapy.Item):
     sid  = scrapy.Field()
     surveynum = scrapy.Field()
     cname = scrapy.Field()
     
class TeacherItem(scrapy.Item):
     className = scrapy.Field()
     teacherName =  scrapy.Field()
     attendance = scrapy.Field()
     knowledge = scrapy.Field()
     patience = scrapy.Field()
     democratic = scrapy.Field()
     strict = scrapy.Field()
     model = scrapy.Field()
     task = scrapy.Field()
     method = scrapy.Field()
     progress = scrapy.Field()
     
class punishmentItem(scrapy.Item):
     className = scrapy.Field()
     teacherName =  scrapy.Field()
     modelRight = scrapy.Field()
     modelNo    = scrapy.Field()
     respectRight = scrapy.Field()
     respectNo   = scrapy.Field()
     insultRight = scrapy.Field()
     insultNo = scrapy.Field()
     hitRight = scrapy.Field()
     hitNo  = scrapy.Field()
     punishRight = scrapy.Field()
     punishNo  = scrapy.Field()
     


