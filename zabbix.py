#!/usr/bin/env python
# -*- coding:utf-8 -*-
#模拟登陆zabbix，获取监控图表并保存至本地
import HTMLParser
import urlparse
import urllib
import urllib2
import cookielib
import string
import os

# 登录的主页面
hosturl = 'http://localhost/zabbix/charts.php?ddreset=1'  # 根据自己的实际地址填写
# post数据接收和处理的页面（我们要向这个页面发送我们构造的Post数据）
posturl = 'http://localhost/zabbix/index.php'  # 从数据包中分析出，处理post请求的url

# 设置一个cookie处理器，它负责从服务器下载cookie到本地，并且在发送请求时带上本地的cookie
cj = cookielib.LWPCookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)

# 打开登录主页面（他的目的是从页面下载cookie，这样我们在再送post数据时就有cookie了，否则发送不成功）
h = urllib2.urlopen(hosturl)

# 构造header，一般header至少要包含一下两项。这两项是从抓到的包里分析得出的。
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1',
           'Referer': '******'}
# 构造Post数据，他也是从抓大的包里分析得出的。
postData = {
    'name': 'admin',  # 用户名
    'password': 'password',  # 密码
    'autologin': 1,
    'enter': 'Sign in'
}

# 需要给Post数据编码
postData = urllib.urlencode(postData)

# 通过urllib2提供的request方法来向指定Url发送我们构造的数据，并完成登录过程
request = urllib2.Request(posturl, postData, headers)
response = urllib2.urlopen(request)
text = response.read()

def get_graph():
    path = '/home/image/'  # 保存图片的地址
    # zabbix的图片的地址的构造
    url = "http://localhost/zabbix/chart2.php?graphid=811&from=now-1h&to=now&profileIdx=web.graphs.filter&profileIdx2=811&width=1200&_=tf58h4s6&screenid="

    img_req = urllib2.Request(url)
    png = urllib2.urlopen(img_req).read()

    file = path +'zabbix_graph_799' + '.png'
    with open(file, 'wb') as f:
        f.write(png)



get_graph()

