# coding=utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@cvte.com
Version: V1.0.0
Date: 2022/9/15 
Desc：
'''

import pytest


def test_one():
    print("测试类之外的方法1")


def test_two():
    print("测试类之外的方法2")


class TestClass:
    def setup_class(self):
        print('类之前')

    def teardowm_class(self):
        print('类之后')

    def setup_method(self):
        print('方法前')

    def teardown_method(self):
        print('方法后')

    def test_one(self):
        assert 1 == 1
        print('测试类里面的方法1')

    def test_two(self):
        assert 'h' in 'hello'
        print('测试类里面的方法2')


if __name__ == '__main__':
    pytest.main(["-s -v", "test_class_01.py"])
