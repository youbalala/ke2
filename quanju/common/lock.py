#coding:utf-8
import requests,time
from common.re_token import get_token

def editlock(token):
    '''修改门锁信息'''
    url="https://test02lm.huohetech.com/lm/lock/edit.do"
    h={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Referer":"https://test02lm.huohetech.com/WEB-INF/pages/lockDetail.html?id=167eea6cac8065"
    }


    body={
        "access_token":token,
        "description":"备注044444",
        "lock_id":"167eea6cac8065",
        "room_code":"房间编号001",
        "house_code":"房源编码002",
        "region_code":"110101",
        "address":"1",
        "house_id":"房屋编号003",
        "operator_code":"2056",
        "channel":"",
        "lock_no":"10.135.1.43",
        "node_id":"",
        "node_no":""
    }
    r=requests.post(url,headers=h,data=body,verify=False)
    print(r.json()["rlt_msg"])
    return r.json()["rlt_msg"]

def delnode(token):
    '''删除网关'''
    delurl="https://test02lm.huohetech.com/lm/node/delete.do"
    body={
        "access_token":token,
        "node_id":"1665c9e226a002"
    }
    h={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Referer":"https://test02lm.huohetech.com/WEB-INF/pages/lockDetail.html?id=167eea6cac8065"
    }
    r2=requests.post(delurl,data=body,headers=h,verify=False)
    print(r2.json())

def addpsw(token):
    '''新增密码'''
    addurl="https://test02lm.huohetech.com/lm/pwd/edit.do"
    h1={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Referer": "https://test02lm.huohetech.com/WEB-INF/pages/lockPassword.html?id=16a43e2c307065"
    }
    body1={
        "access_token":token,
        "lock_id":	"16a43e2c307065",
        "pwd_group":"6",
        "pwd_text":"",
        "pwd_user_name":"11",
        "pwd_user_mobile":"18500045564",
        "valid_time_start":"1555988658000",
        "valid_time_end":"1556593458000",
        "description":"",
        "send_sms_flag":"Y",
        "pwd_type":"0"
    }
    r3=requests.post(url=addurl,data=body1,headers=h1,verify=False)
    print(r3.json())


def delpsw(token):
        '''删除密码'''
        url4="https://test02lm.huohetech.com/lm/pwd/disable.do"
        h2={
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
            "Referer": "https://test02lm.huohetech.com/WEB-INF/pages/lockPassword.html?id=16a43e2c307065"

        }
        body2={
            "access_token":token,
            "pwd_no":	"8",
            "lock_id":	"16a43e2c307065",
            "op_type":	"3"

        }
        r4=requests.post(url=url4,data=body2,headers=h2,verify=False)
        print(r4.json())

def getid(token,phone):
    '''获取被授权人id'''
    url="https://test02lm.huohetech.com/lm/common/user/list.do"
    h={
        "Referer": "https://test02lm.huohetech.com/WEB-INF/pages/lockManager.html?id=16a24f11c1d065",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
    b={
        "access_token":token,
        "keyword":	phone,  #被授权人手机号
        "role_code":"0"
    }
    r6=requests.post(url,headers=h,data=b,verify=False)
    id=r6.json()["data"]["rows"][0]["user_id"]
    print(id)
    return id

def shouquan(token,id):
    '''给用户授权'''
    url5="https://test02lm.huohetech.com/lm/lock/auth.do"
    h5={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Referer": "https://test02lm.huohetech.com/WEB-INF/pages/lockManager.html?id=16a24f11c1d065"
    }
    b5={
        "access_token":token,
        "op_type":"0",
        "lock_id":	"16a535aae7c065",  #门锁编号
        "rcv_id":	id, #被授权人id
        "auth_time_start":"1557227385000",
        "auth_time_end":"1872846585000",
        "remark_user_name":	"1234",
        "description":"",
        "allow_auth":	"Y",
        "allow_operate_pwd":	"Y"
    }
    r5=requests.post(url=url5,data=b5,headers=h5,verify=False)
    print(r5.json())

def del_shoquan(token,id):
    '''删除授权用户'''
    url6="https://test02lm.huohetech.com/lm/lock/auth_batch.do"
    b6={
        "access_token":token,
        "lock_id":"16a535aae7c065",
        "rcv_id":id, #被授权人id
        "op_type":"1"

    }
    r6=requests.post(url6,data=b6,verify=False)
    print(r6.json())





if __name__=="__main__":
    token=get_token()
    # addpsw(token)
    # delpsw(token)

    id=getid(token)
    shouquan(token,id)

    del_shoquan(token,id)