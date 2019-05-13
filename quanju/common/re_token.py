#coding:utf-8
import yaml
import os

cur=os.path.dirname(os.path.realpath(__file__))
def get_token(yamlname="token.yaml"):
    '''从token.yaml读取token值：
        param yamlname:配置文件名称
        ：return：token值
    '''
    p=os.path.join(cur,yamlname)
    f=open(p)
    a=f.read()
    print(a)
    t=yaml.load(a) #用load方法转成字典
    print(t)
    f.close()
    return t["token"]
if __name__=="__main__":
    print(get_token())