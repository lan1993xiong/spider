# -*- coding: utf-8 -*-

import pymysql
from twisted.enterprise import adbapi
from scrapy.utils.project import get_project_settings  #导入seetings配置
import sys
class DBHelper():
    '''这个类也是读取settings中的配置，自行修改代码进行操作'''
    sys.path.append('D:\WebCrawlSpider\WebCrawlSpider\dbhelper.py')
    def __init__(self):
        
        settings = get_project_settings()  #获取settings配置，设置需要的信息
 
        dbparams = dict(
            host=settings['MYSQL_HOST'],  #读取settings中的配置
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',  #编码要加上，否则可能出现中文乱码问题
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=False,
        )
        #**表示将字典扩展为关键字参数,相当于host=xxx,db=yyy....
        dbpool = adbapi.ConnectionPool('pymysql', **dbparams)
        self.dbpool = dbpool

    def connect(self):
        return self.dbpool

    #插入数据
 #   def insertSurvey(self, item):
        #这里定义要插入的字段
 #       sql = "insert into bldata(surveyId,cName,surveyNum) values(%s,%s,%s)"
        #调用插入的方法
 #       query = self.dbpool.runInteraction(self._conditional_insert_survey_table, sql, item)
        #调用异常处理方法
 #       query.addErrback(self._handle_error)
  #      return item
    
  #  def _conditional_insert_survey_table(self, canshu, sql, item):
        #取出要存入的数据，这里item就是爬虫代码爬下来存入items内的数据
   #     params = (item['surveyId'],  item['cName'],item['surveyNum'])
   #     canshu.execute(sql, params)  
     
   
  #  def insertTeacherTable(self, item):
        #这里定义要插入的字段
     #   sql = "insert into teacher(className,teacherName,attendance,knowledge,patience,strict,model,democratic,task,method,progress)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        #调用插入的方法
     #   query = self.dbpool.runInteraction(self._conditional_insert_teacher_table, sql, item)
        #调用异常处理方法
     #   query.addErrback(self._handle_error)
        
    #    return item

    #写入数据库中
    #def _conditional_insert_teacher_table(self, canshu, sql, item):
        #取出要存入的数据，这里item就是爬虫代码爬下来存入items内的数据
    #    params = (item['className'], item['teacherName'], item['attendance'],item['knowledge'], item['patience'], item['strict'],item['model'], item['democratic'], item['task'], item['method'], item['progress'])
     #   canshu.execute(sql, params)

 
    def _insert(self,item,sql,params):
         #调用插入的方法
         query = self.dbpool.runInteraction(self._conditional_insert, sql, item,params)
         #调用异常处理方法
         query.addErrback(self._handle_error)
         return item
    
    
    def _conditional_insert(self, canshu, sql, item,params):
       
         canshu.execute(sql, params) 
    
    #插入调查人数的表
    def _insert_survey(self, item):
          self.params = (item['sid'],item['cname'],item['surveynum'])
          self.sql = "insert into bldata(sid,cName,surveyNum) values(%s,%s,%s)"
          self._insert(item,self.sql,self.params)
          
    #插入教师情况表
    def _insert_teacher(self,item):
         sql = "insert into teacher(class_name,teacher_name,attendance,knowledge,patience,strict,model,democratic,task,method,progress)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
         
         params = (item['className'], item['teacherName'], item['attendance'],item['knowledge'], item['patience'], item['strict'],item['model'], item['democratic'], item['task'], item['method'], item['progress'])
         
         self._insert(item,sql,params) 
    
    #插入体罚表
    def _insert_punish(self,item):
          sql = "insert into punish(class_name,teacher_name,model_right,model_no,respect_right,respect_no,insult_right,insult_no,hit_right,hit_no,punish_right,punish_no)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
         
          params = (item['className'], item['teacherName'], item['modelRight'],item['modelNo'], item['respectRight'], item['respectNo'],item['insultRight'], item['insultNo'], item['hitRight'], item['hitNo'], item['punishRight'], item['punishNo'])
         
          self._insert(item,sql,params) 
         
    #错误处理方法
    def _handle_error(self, failue):
        print('--------------database operation exception!!-----------------')
        print(failue)
        