#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import json
import requests

#钉钉机器人地址
api_url = 'https://oapi.dingtalk.com/robot/send?access_token=42fbxxxxxxxxxxxxxxxxxxxxxx'

headers = {'Content-Type':'application/json;charset=utf-8'}

def msg(text):
    json_text={
        "msgtype":"text",
        "text":{
            "content":text
        },
        "at":{
            "atMobiles":[
                "186..."         # @的人的手机号
            ],
            "isAtAll":False           # 是否@全员
        }
    }
    print requests.post(api_url,json.dumps(json_text),headers=headers).content

if __name__ == '__main__':
    text = sys.argv[1]
    msg(text)
