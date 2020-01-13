# -*- coding: utf-8 -*-
import pymysql
import requests
import re
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


ua = UserAgent().random
headers = {
    'User-Agent':ua
}

db = pymysql.connect("localhost", "root", "root", "xici_proxy")
cursor = db.cursor()
num = 0
for i in [1,2,3,4,5]:
    tar_url = 'https://www.xicidaili.com/wn/'+str(i)
    req = requests.get(tar_url,headers = headers)
    readText = req.text
    #正则表达式
    compileModels =('''
      <td>(.*?)</td>
      <td>(.*?)</td>
      <td>
        <a href=(.*?)>(.*?)</a>
      </td>
      <td class="country">(.*?)</td>
      <td>(.*?)</td>''')
    pattern = re.compile(compileModels)
    compileText = pattern.findall(readText)
    for i in compileText:
        print(list(i))
        sql = """INSERT INTO xicidaili(ip,port,herf, 服务器地址, 是否匿名, 类型) VALUES (%s,%s,%s,%s,%s,%s)"""
        cursor.execute(sql,(i))
        db.commit()
db.close()