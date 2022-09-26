# coding=utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@cvte.com
Version: V1.0.0
Date: 2022/9/15 
Desc：
'''
import pytest


@pytest.fixture()
def open_browser():
    print('\n打开浏览器，打开百度首页')
    yield
    print('执行teardown')
    print('组后关闭浏览器')


def test_open(login):
    print({"case1": "名字"})

@pytest.mark.usefixtures('open_browser')
def test_case():
    print("你来了")

@pytest.mark.usefixtures('open_browser')
def test_token():
    print("我要走了")

if __name__ == '__main__':
    pytest.main(['-s', 'test_usefixture.py'])
