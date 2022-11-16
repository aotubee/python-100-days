#!/usr/bin/env python3
#coding=utf-8

import time
import hmac
import hashlib
import base64
import requests
import json
import urllib.parse


#钉钉机器人的timestap和加签，加签在设置钉钉机器人时生成。下面代码引用钉钉加签说明文档
timestamp = str(round(time.time() * 1000))
secret = 'SEC8977ad824079c46935488be99fb3bc87f92a61886c21ad03bdc312cf3ed1c0a0'
secret_enc = secret.encode('utf-8')
string_to_sign = '{}\n{}'.format(timestamp, secret)
string_to_sign_enc = string_to_sign.encode('utf-8')
hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
#print (timestamp)
#print (sign)

#https://oapi.dingtalk.com/robot/send?access_token=XXXXXX&timestamp=XXX&sign=XXX

token='867b3499753420ea8d9f4d67e560c27e6965594e58ecfd9c5283f4b9156643db'
webhook ='https://oapi.dingtalk.com/robot/send?access_token=' + token + '&timestamp=' + timestamp + '&sign=' + sign
#print (webhook)

data = {
    "msgtype": "text",
    "text": { "content": "测试" },
    #@群成员
    "at": {"atMobiles": ["18602900290"]},
    "isAtAll": False }

headers={'Content-Type': 'application/json'}   #定义数据类型
req = requests.post(webhook, data=json.dumps(data), headers=headers)   #发送post请求
#req = requests.get(url=webhook)
html = req.text
print(html)
print(json.dumps(data))
