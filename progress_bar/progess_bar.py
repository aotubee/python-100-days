#!/sr/bin/env python3
# coding=utf-8

import time
import sys

def progress_bar():
    for i in range(101):
        #回到行首,执行过程中将上一次所显示的覆盖
        sys.stdout.write('\r')
        sys.stdout.write("%s%% :%s" %(int(i%101), int(i%101)*'#'))
        sys.stdout.flush()
        time.sleep(0.1)
    #执行完毕后换行
    sys.stdout.write('\n')

if __name__=='__main__':
    progress_bar()
