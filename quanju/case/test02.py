#coding:utf-8
import unittest
from common.re_token import get_token
from common.lock import editlock , delnode,addpsw,delpsw,getid,shouquan,del_shoquan
class Test_01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.token=get_token()
        print("获取当前用例token值：%s"%cls.token)
    def test01(self):
        '''测试用例1新增授权用户'''
        id=getid(self.token,18500045564)
        shouquan(self.token,id)
        # self.assertEqual()
        print("用例1测试通过")

    def test02(self):
        '''删除授权用户'''
        id=getid(self.token,18500045564)
        # shouquan(self.token,id)
        del_shoquan(self.token,id)
        print("用例2测试通过")

    def test03(self):
        '''新增密码'''
        addpsw(self.token)
        print("用例3测试通过")

    def test04(self):
        '''删除密码'''
        delpsw(self.token)
        print("用例4测试通过")
if __name__=="__main__":
    unittest.main()