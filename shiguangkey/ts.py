import requests

class MyGet:

  def __init__(self):
    self.headers = ({
      # "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0",
      # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
      # "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
      # "Accept-Encoding": "gzip, deflate, br",
      # "Connection": "keep-alive",
      # "Cookie": "Hm_lvt_7e8b931a9b138d095673181619178304=1623069026,1623156777; token=e491630507100d5621deb494297add77; im-token=e491630507100d5621deb494297add77; aliyungf_tc=cd17ceb8a46854c91f9ae95e4ba47ec8a2c6fbe7f651262b2eaa68dcfc19127e",
      # "Upgrade-Insecure-Requests": "1",
      # "Cache-Control": "max-age=0",
      # "TE": "Trailers",
      "Cookie": "Hm_lvt_7e8b931a9b138d095673181619178304=1623069026,1623156777; token=e491630507100d5621deb494297add77; im-token=e491630507100d5621deb494297add77;",
    })

  def get(self):
    # 获取课程名
    url = "https://open.shiguangkey.com/live/course/get?courseId=17111"
    result = requests.get(url = url, headers = self.headers)
    print(result.text)

  def getVideoUrlForUser(self):
    # 获取ts文件名
    url = "https://www.shiguangkey.com/api/course/getVideoUrlForUser?videoId=435085&terminalType=4"
    result = requests.get(url = url, headers = self.headers)
    print(result.text)

  def listChapterInfo(self):
    # 获取课时
    url = "https://www.shiguangkey.com/api/courses/listChapterInfo?classId=17199&terminalType=4"
    result = requests.get(url = url, headers = self.headers)
    print(result.text)

if __name__ == '__main__':
  myGet = MyGet()
  myGet.getVideoUrlForUser()