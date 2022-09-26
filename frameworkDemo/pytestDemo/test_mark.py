# coding=utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@cvte.com
Version: V1.0.0
Date: 2022/9/15 
Desc：
'''

import pytest

test_user_data = ["san", "qian", "wang"]
@pytest.fixture()
def login_r(request):
    user = request.param
    print("\n打开首页准备登录，登录用户名%s" % user)
    return user


@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+5", 7), ("7*5", 35)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected


@pytest.mark.parametrize("login_r", test_user_data, indirect=True)
def test_login(login_r):
    a = login_r
    print('测试用例的返回值%s' % a)
    assert a != ""


if __name__ == '__main__':
    pytest.main(['-q', 'test_mark.py'])
