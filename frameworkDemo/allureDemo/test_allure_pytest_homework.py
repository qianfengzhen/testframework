# coding=utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@cvte.com
Version: V1.0.0
Date: 2022/9/20 
Desc：
'''

import pytest
import allure
import os

test_data1 = [{'user': 'qian', 'password': '345'}]

@allure.feature("登录测试用例")
@pytest.mark.parametrize("login", test_data1, indirect=True)
def test_login(login):
    user = login['user']
    pwd = login['password']
    print("登录成功")
    assert 1 == True
    return user,pwd


@allure.feature("人力资源模块测试用例")
@pytest.mark.parametrize("login",test_data1, indirect=True)
def test_add_member(login):
    with allure.story('这是增加人员的操作'):
        with allure.step('这是'):
            pass

    with allure.story('这是删除人员操作'):
        pass

    with allure.story('这是修改人员操作'):
        pass

    with allure.story('这是查询人员操作'):
        pass


if __name__ == '__main__':
    pass