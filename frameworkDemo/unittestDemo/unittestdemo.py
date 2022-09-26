# coding=utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@cvte.com
Version: V1.0.0
Date: 2022/9/14 
Desc：
'''

import time
import unittest
import requests
import os

# from frameworkDemo.unittestDemo.calculate import *
# from frameworkDemo.unittestDemo.HTMLTestRunner import *
from calculate import *
from HTMLTestRunner import *

class TestClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("测试整个类必须执行的方法")

    def setUp(self) -> None:
        print("每一个测试方法前运行的方法，准备数据")

    def tearDown(self) -> None:
        print("每一个方法后运行的方法")

    def test_one(self):
        print("这是测试方法1")
        assert 1 == 1
        self.assertIn("l", "hello")
        res = requests.get('https://www.baidu.com')
        print(res.text)

    def test_second(self):
        print("这是测试方法2")
        assert 1 == 1
        assert {'name': 'linda', 'age': 18} == {'name': 'linda', 'age': 188}
        a = 'hello'
        age = 35
        assert a in 'helloworld'
        print("这是测试方法2，研究一下unittest的断言方法")
        self.assertGreater(1, 2, msg='这是不可能')
        self.assertIn(a, 'world', msg='没有hello')

    def test_third(self):
        print("这是测试方法3-单元测试-测试计算器代码")
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(4, add(2, 2))
        self.assertEqual(2, minus(6, 4))

    @classmethod
    def tearDownClass(cls) -> None:
        print("测试整个类后执行的方法")


if __name__ == '__main__':
    # unittest.main(verbosity=2)
    report_path = os.path.join(os.path.dirname(__file__), 'report')
    if os.path.exists(report_path):
        print('文件已经存在')
    else:
        try:
            os.mkdir(report_path)
            print('创建文件成功')
        except Exception as e:
            print(e)
            # os.makedirs(report_path)

    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    filename = report_path + "/" + now + "_result.html"
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestClass))
    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner(stream=fp, title='测试报告', description='测试用例')
        runner.run(suite)