# coding=utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@cvte.com
Version: V1.0.0
Date: 2022/9/19 
Desc：
'''
import os

import allure
import pytest


@allure.feature('购物车功能')
class TestShoppingTrolley():
    @allure.story('加入购物车')
    def test_add_shopping_trolley(self):
        with allure.step('浏览商品'):
            login_shopping('qian', '8888')
            allure.attach('商品1', '三星')
        with allure.step('点击商品'):
            pass
        with allure.step('效验结果'):
            allure.attach('期望结果', '添加购物车成功')
            allure.attach('实际结果', '添加购物车失败')
            assert 'success' != 'failed'

    @allure.story('修改购物车')
    def test_change_shopping(self):
        with allure.step('浏览商品'):
            allure.attach('商品1', '三星')
        with allure.step('点击删除'):
            allure.attach('期望结果', '删除成功')
            allure.attach('实际结果', '删除成功')
            assert 'success' == 'success'


@allure.step('登录')
def login_shopping(user, pwd):
    print(user, pwd)


if __name__ == '__main__':
    pytest.main(['--alluredir=./report/', 'test_allure_shopping.py'])
    os.system('allure serve ./report')
