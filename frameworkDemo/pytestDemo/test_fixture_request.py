# coding=utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@cvte.com
Version: V1.0.0
Date: 2022/9/15 
Desc：
'''


import pytest

test_data = [1,2,3,'linda']

@pytest.fixture(params=test_data)
def test_data(request):
    return request.param


def test_one(test_data):
    print('\n现在搜索%s'%test_data)


if __name__ == '__main__':
    pytest.main(['-s','test_fixture_request.py'])
