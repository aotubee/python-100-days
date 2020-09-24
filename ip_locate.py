#!/usr/bin/env python3
# coding=utf-8

import re
from bs4 import BeautifulSoup
from urllib import request

qurl=r'http://ip138.com/ips1388.asp?ip=%s&action=2'

headers={'Host':'ip138.com',
'Connection':'keep-alive',
'Cache-Control':'max-age=0',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.9',
'Cookie':'pgv_pvi=3646356480; Hm_lvt_f4f76646cd877e538aa1fbbdf351c548=1574747938; Hm_lpvt_f4f76646cd877e538aa1fbbdf351c548=1574747938; ASPSESSIONIDSSSSTSRQ=OBBDOKKBPLHMGKJCHEHEEPDF; Hm_lvt_b018ba5033f3b0d184416653ad858a48=1574747980; Hm_lpvt_b018ba5033f3b0d184416653ad858a48=1574748157'
}

def ip_addr(ip):
    addr=None
    req= request.Request(qurl%ip)
    for k,v in headers.items():
        req.add_header(k,v)
    resp= request.urlopen(req,timeout=10).read()
    
    soup=BeautifulSoup(resp.decode('gbk'),'html.parser')
    tds=soup.find_all('ul',class_='ul1')
    if len(tds)>0:
        addr=tds[0].findChildren()[0].text
        addr=re.sub(r'本站数据：(.*)',r'\1',addr).strip()
        return addr
    
print(ip_addr('47.240.19.112'))
