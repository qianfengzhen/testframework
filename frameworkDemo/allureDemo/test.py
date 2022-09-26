# coding=utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@cvte.com
Version: V1.0.0
Date: 2022/9/20 
Desc：
'''

from os.path import dirname,abspath

if __name__ == '__main__':
    a = dirname(dirname(__file__))+'/driver/chromedriver'
    print(a)
