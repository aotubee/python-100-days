#!/usr/bin/env python3
# coding=utf-8

import subprocess
import multiprocessing

def check_alive(ip):
    #使用subprocess.call返回一个状态码,若通则为0。
    result=subprocess.call("ping -w 4 -n %s" %ip,stdout=subprocess.PIPE,shell=True)
    if result==0:
        str=subprocess.getoutput('ping -w 4 -n %s' %ip)
        #通过切片获取平均延时的值
        info=(str.split()[-2].split('/')[1])
        print ("可以ping通，平均延迟为：%s ip:%s" %(info,ip))
        with open('can_ping.log','a') as f:
            f.write(ip + '\n') 
    else:
        print ('此IP不通.%s' %ip)

if __name__=="__main__":
    ips="192.168.88."
    for i in list(range(1,255)):
        ip= ips + str(i)
        print ("IP网络测试情况：")
        check_alive(ip)
