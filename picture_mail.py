#!/usr/bin/env python
# -*- coding:utf-8 -*-
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

import time

mailto_list=['xxxxxxxx@qq.com']   # 收件人列表
mailcc_list=['xxxxxxxx@qq.com']   # 抄送列表
mail_host="smtp.qq.com:25"   # 邮件服务器
mail_user="xxxxxxxx@qq.com"              # 用户名
mail_pass="xxxxxxxxx"                # 密码
mail_postfix="qq.com"        #  邮件后缀

html = """<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<p>
服务器192.168.100.51  net 的1h截图<br>
<img src="cid:net_traffic" />
</p>
"""

def send_mail(to_list, cc_list, sub):
    # 增加图片
    def addimg(src, imgid):
        fp = open(src, 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()
        msgImage.add_header('Content-ID', imgid)
        return msgImage

    msg = MIMEMultipart('related')
    #HTML代码
    msgtext = MIMEText(html, "html", "utf-8")
    msg.attach(msgtext)

    # 全文件路径，后者为ID 根据ID在HTML中插入的位置
    msg.attach(addimg("/home/image/zabbix_graph_799.png", "net_traffic"))

    me = mail_user + "@" + mail_postfix
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ",".join(to_list)
    msg['Cc'] = ",".join(cc_list)
    send_to = to_list + cc_list
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user, mail_pass)
        server.sendmail(me, send_to, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False

if __name__ == '__main__':
    title = "zabbix监控数据" + time.strftime('%Y%m%d',time.localtime(time.time()))
    if send_mail(mailto_list,mailcc_list,title):
        print "邮件发送成功"
    else:
        print "邮件发送失败"
