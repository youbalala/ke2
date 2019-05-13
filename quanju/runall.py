#coding:utf-8
import unittest
import os
import yaml
from common import HTMLTestRunner_cn
from ruamel import yaml
import requests
curpath=os.path.dirname(os.path.realpath(__file__))

def login(user,psw):
    '''先登录，传账号密码两个参数'''
    url="https://test02lm.huohetech.com/lm/common/user/login_with_image"
    body={
    "account":user,
    "password":psw,
    "source":"10"

    }
    h={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Referer": "https://test02lm.huohetech.com/",
    "Origin": "https://test02lm.huohetech.com",
    "X-Requested-With": "XMLHttpRequest",
    "Accept-Language": "zh-CN,zh;q=0.8"
  }
    a=requests.post(url,data=body,headers=h,verify=False)
    #print(a.json())
    token=a.json()["data"]["access_token"]#登录后获取到的token值
    print(token)
    return token
def write_yaml(value):
    '''把获取到的token值写入到yaml文件'''
    ypath=os.path.join(curpath,"common","token.yaml")
    print(ypath)
    #需写入的内容
    t={"token":value}
    # 写入到yaml文件
    with open(ypath, "w", encoding="utf-8") as f:
        yaml.dump(t, f, Dumper=yaml.RoundTripDumper)
def all_case(rule="test*.py"):
    '''加载所有用例'''
    case_path=os.path.join(os.path.dirname(os.path.realpath(__file__)),"case")
    discover=unittest.defaultTestLoader.discover(case_path,
                                                 pattern=rule,
                                                 top_level_dir=None
                                                 )
    return discover
def run_case(all_case,reportname="report"):
     '''执行所有用例，并把结果写入HTML测试报告'''
     curpath=os.path.dirname(os.path.realpath(__file__))
     report_path=os.path.join(curpath,reportname)
     #如果不存在这个文件夹，就创建一个
     if not os.path.exists(report_path):
         os.mkdir(report_path)
     report_abspath=os.path.join(report_path,"result.html")
     print("report path:%s"%report_abspath)
     fp=open(report_abspath,"wb")
     runner=HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                              verbosity=2,
                                              title=u"自动化测试报告,测试结果如下",
                                              description=u"用例执行情况" )
     runner.run(all_case)
     fp.close()

if __name__=="__main__":
    token=login("whinstaller","huohe4485")
    write_yaml(token) #写入yaml
    allcases=all_case()  #加载用例
    run_case(allcases)
