# coding=utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@cvte.com
Version: V1.0.0
Date: 2022/9/18 
Desc：
'''
import os

import pytest


@pytest.mark.android
def test_one():
    print(1)


@pytest.mark.web
def test_two():
    print(2)


@pytest.mark.ios
def test_three():
    print(3)

@pytest.mark.use
def test_four():
    for a in range(1, 5, 1):
        os.system('ping 127.0.0.1')
    print("第四个测试用例 延时完成")

#
# if __name__ == '__main__':
#     # os.system('pytest -s test_mark_zi.py -m=ios')
#     pytest.main()
