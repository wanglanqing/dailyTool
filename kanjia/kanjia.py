# -*- coding: utf-8 -*-
# @Time    : 2019/7/29 15:02
# @Author  : wanglanqing


#encoding:utf-8
import MySQLdb as mysql ,time,datetime,calendar
from openpyxl import Workbook

def myc(env):
    # db = mysql.connect(host='221.122.127.183',user='voyager',passwd='voyager',db='voyager',port=5701,charset='utf8')
    if env=='testvoyager':
        db = mysql.connect(host='172.16.105.12',user='voyager',passwd='voyager',db='voyager',port=5701,charset='utf8')
    if env=='testtest':
        db = mysql.connect(host='172.16.105.12',user='voyager',passwd='voyager',db='test',port=5701,charset='utf8')
    if env=='devvoyager':
        db = mysql.connect(host='123.59.17.42',user='voyager',passwd='SIkxiJI5r48JIvPh',db='voyagerlog',port=3306,charset='utf8')
    if env=='nomandytest':
        db = mysql.connect(host='172.16.105.12',user='voyager',passwd='voyager',db='normandy',port=5701,charset='utf8')

    db.autocommit(True)
    myc=db.cursor()
    return myc,db
def selectsql(env,sql):
    tmpmyc,tmpdb=myc(env)
    try:
        tmpmyc.execute(sql)
        result=tmpmyc.fetchall()
    except:
        raise SystemError
    tmpmyc.close()
    tmpdb.close()
    return result
def execsql(env,sql):
    tmpmyc,tmpdb=myc(env)
    try:
        tmpmyc.execute(sql)
        tmpdb.commit()
    except Exception as e :
        print 'error is {}'.format(e.message)
    return tmpmyc.rowcount

# if __name__ == '__main__':
#     tmpsql='''SELECT ad_click_tag FROM voyagerlog.ad_click_log20180930 where ad_choosen_tag='D3W1CD6R1IIZXEMSKH' '''
#     re=selectsql('testvoyager',tmpsql)
#     print re
#     print re[0][0]
#     print type(re[0][0])


import requests, time, json,threading,random


# 生成随机手机号
def getphone():
    tmplist = ['1', '2', '3', '4', '5', '6', '7', '8']
    # tmplist=['1','2','3']
    tmpphonelist = []
    phone = '179423{}{}{}{}{}'.format(random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9))
    # tmpphonelist.append(phone)
    # print tmpphonelist
    return phone


# 根据手机号获取最新的验证码
def getcode(phone):
    tmpsql = '''SELECT left(msg,18) from normandy.phone_send_record where phone='{0}' ORDER BY id desc LIMIT 1;'''.format(str(phone))
    re = selectsql('nomandytest', tmpsql)
    tmpcode = str(re[0][0][-6:])
    'phone:{0},code:{1}'.format(phone, tmpcode)
    return tmpcode


def login():
    r = requests.session()
    # 手机号list
    phone = getphone()
        # 注册接口 发送验证码
    result1 = r.get('http://api.chinayoupin.com/user/loginSms.htm?sendType=lOGIN_SMS&phone={0}'.format(str(phone)))
    json.dumps(result1.json(), ensure_ascii=False, encoding='UTF-8')
    # 验证码发送成功走下面流程，登录，砍价
    if result1.json()['code'] == 200:
        # 获取验证码
        code = getcode(phone)
        # 调用登录接口，登陆后r中自带cookie
        result2 = r.get('http://api.chinayoupin.com/user/login.htm?code={0}&phone={1}'.format(code, str(phone)))
        json.dumps(result2.json(), ensure_ascii=False, encoding='UTF-8')
    return r

def kanjia(r,taskId,event):
    # 调用砍价接口,写死了砍价任务id358 ，根据实际情况控制
    print 'kan ing', time.time()
    result3 = r.get('http://api.chinayoupin.com/bargain/task/log/userBargain.htm?taskId={}'.format(taskId))
    print json.dumps(result3.json(), ensure_ascii=False, encoding='UTF-8')




class LoopAdDatas(threading.Thread):
    def __init__(self):
        super(LoopAdDatas, self).__init__()
        self.__flag = threading.Event()
        self.__flag.set()
        self.__running = threading.Event()
        self.__running.set()

    def run(self):
        # for i in range(5):
        # print 'run time is : ' , time.time()
        kanjia(login(), 394)
        self.stop()

    def stop(self):
        self.__flag.set()
        self.__running.clear()

if __name__ == '__main__':
    # 注意指定host在测试环境执行 101.254.242.11 api.chinayoupin.com
    # for i in range(25):
    #     print 'count : ', i
    #     # r =login()
    #     #la = LoopAdDatas()
    #     #la.start()

    readis_ready = threading.Event()
    t1 = threading.Thread(target=kanjia, args=(login(), 394,readis_ready,), name='t1')
    t2 = threading.Thread(target=kanjia,args=(login(), 394,readis_ready,), name='t2')
    t3 = threading.Thread(target=kanjia, args=(login(), 394,readis_ready,), name='t3')
    t4 = threading.Thread(target=kanjia, args=(login(), 394,readis_ready,), name='t4')
    t5= threading.Thread(target=kanjia,args=(login(), 394,readis_ready,), name='t5')
    t6= threading.Thread(target=kanjia,args=(login(), 394,readis_ready,), name='t5')
    t7= threading.Thread(target=kanjia,args=(login(), 394,readis_ready,), name='t5')
    t8= threading.Thread(target=kanjia,args=(login(), 394,readis_ready,), name='t5')
    t9= threading.Thread(target=kanjia,args=(login(), 394,readis_ready,), name='t5')
    t11= threading.Thread(target=kanjia,args=(login(), 394,readis_ready,), name='t5')
    t12= threading.Thread(target=kanjia,args=(login(), 394,readis_ready,), name='t5')


    print 'result ----'
    a1 = time.time()
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t11.start()
    t12.start()
    a2 = time.time()
    print'qqqq',a2 - a1
