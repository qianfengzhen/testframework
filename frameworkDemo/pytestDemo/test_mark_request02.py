# coding = utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@cvte.com
Version: V1.0.0
Date: 2022/9/16 
Desc：
'''
import sys

import pytest

test_user_data = [{'user': 'qian', 'password': '1234'},
                  {'user': 'feng', 'password': '123'}]

test_data = ['unittest', 'pytest']


@pytest.fixture()
def login_r(request):
    user = request.param['user']
    password = request.param['password']
    print('\n打开首页，使用用户名%s,使用密码%s' % (user, password))
    if password:
        return True
    else:
        return False

@pytest.fixture()
def getname(request):
    return request.param


@pytest.mark.parametrize("getname", test_data, indirect=True)
@pytest.mark.parametrize("login_r", test_user_data, indirect=True)
def test_login(login_r, getname):
    a = login_r
    b = getname
    print("测试用例中login返回的值:%s" %a)
    print("测试用例中getname的返回值：%s" %b)
    assert a != "" or b != ""

@pytest.mark.skip()
def test_skip():
    print("第二个测试用例")
    assert 1 != 2

@pytest.mark.skipif (sys.platform == 'win32' ,reason= "不存在这样的平台")
def test_skipif(login):
    print("第三个测试某些条件下跳过")


if __name__ == '__main__':
    pytest.main(['-v', 'test_mark_request01.py'])
