#coding:utf-8
import unittest
from common.re_token import get_token
from common.lock import editlock , delnode,addpsw
class Test_01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.token=get_token()
        print("获取当前用例token值：%s"%cls.token)
    def test01(self):
        '''测试用例1'''
        body1={
            "a":"111111",
            "b":"111111",
            "token":self.token #参数关联

        }
        print("用例1body：%s"%body1)
    def test02(self):
        '''测试用例2'''
        body1={
            "a":"222222",
            "b":"222222",
            "token":self.token #参数关联
        }
        print("用例2body：%s"%body1)

    def test03(self):
        print("测试用例3")
        m=editlock(self.token)
        self.assertEqual(m,u"成功")

    def test04(self):
        print("测试用例4")
        m=delnode(self.token)
        self.assertEqual(m,u"成功")
    def test05(self):
        print("测试用例4")
        m=addpsw(self.token)
        self.assertEqual(m,u"成功")

if __name__=="__main__":
    unittest.main()