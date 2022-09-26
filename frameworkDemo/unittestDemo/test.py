# coding=utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@cvte.com
Version: V1.0.0
Date: 2022/9/15 
Desc：
'''

import os

if __name__ == '__main__':
    report_path = os.path.join(os.path.dirname(__file__), 'report1')
    print(os.path.exists(report_path))

    if os.path.exists(report_path):
        print('文件已存在不需要创建')
    else:
        try:
            os.mkdir(report_path)
        except Exception as e:
            os.makedirs(report_path)

