# -*- coding: utf-8 -*-
 
class transCookie:
  def __init__(self, cookie):
     self.cookie = cookie
 
  def stringToDict(self):
 
     itemDict = {}
     items = self.cookie.split(';')
     for item in items:
        key = item.split('=')[0].replace(' ', '')
        value = item.split('=')[1]
        itemDict[key] = value
     return itemDict
 
if __name__ == "__main__":
  cookie = 'Cookie: acw_tc=2f624a7515417481353322827e0e6e94356a8e379c805879b6e5410ad74e51; .ASPXANONYMOUS=QgdLx46u1AEkAAAAZDQxMmU2ZWYtNGU1NC00YWQ2LTlhYzUtYWFhODQ4YWNhMzFhllQf2IlaO0TRNIg081s8mNToHf01; WjxUser=UserName=13602565101&Type=1; UM_distinctid=166f75990786f-05ee501c653b4e-b79183d-100200-166f759907bd6; baidutgkey=%u95EE%u5377%u661FBH%7C2%7Cbaidu; mobileuser=13602565101; mqcount=4; spiderregkey=baidu.com%c2%a7%e7%9b%b4%e8%be%be%c2%a71; _cnzz_CV4478442=%E7%94%A8%E6%88%B7%E7%89%88%E6%9C%AC%7C%E4%BC%81%E4%B8%9A%E7%89%88%7C1543201343943; CNZZDATA4478442=cnzz_eid%3D2031174633-1541745833-https%253A%252F%252Fwww.wjx.cn%252F%26ntime%3D1543228158; Hm_lvt_21be24c80829bd7a683b2c536fcf520b=1543158466,1543194802,1543200919,1543228527; Hm_lpvt_21be24c80829bd7a683b2c536fcf520b=1543228527; SojumpSurvey=010220D8DBE88A53D608FE2078ED6FAC53D608001A4B623A672875376231006D007500750069006B0065007A007A00750079007400760032006F00320072006600310072006300610000012F00FF8A88DFDB85FD82C8A934945E34A2DC356375D130; logcook=1'
  trans = transCookie(cookie)
  print (trans.stringToDict())
