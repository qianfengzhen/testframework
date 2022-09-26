# coding = utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@cvte.com
Version: V1.0.0
Date: 2022/9/16 
Desc：
'''

import requests
import pytest

test_user_data = [{'user': 'qian', 'password': '1234'},
                  {'user': 'feng', 'password': '123'}]

@pytest.fixture()
def login_r(request):
    user = request.param['user']
    password = request.param['password']
    print('\n打开首页，使用用户名%s,使用密码%s' % (user, password))
    if password:
        return True
    else:
        return False

@pytest.mark.parametrize("login_r", test_user_data, indirect=True)
def test_login(login_r):
    a = login_r
    print("测试用例中login返回的值:%s" %a)
    assert a != ""


if __name__ == '__main__':
    pytest.main(['-v', 'test_mark_request01.py'])
