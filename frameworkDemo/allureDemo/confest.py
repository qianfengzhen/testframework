# coding=utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@cvte.com
Version: V1.0.0
Date: 2022/9/21 
Desc：
'''
import pytest


@pytest.fixture()
def login(request):
    user = request.param['user']
    pwd = request.param['pwd']
    return user, pwd

