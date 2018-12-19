# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 17:38
# @Author  : wanglanqing

import datetime,time,json
import requests

class cpaData(object):
    def __init__(self,appKey=None,startTime=None,endTime=None,pageNum=None,pageSize=20):
        self.appKey=appKey
        self.startTime=startTime
        self.endTime=endTime
        self.pageNum=pageNum
        self.pageSize=pageSize
        self.ts = int(time.time())
        pass


#获得当前时间，转换为时间戳
    # @staticmethod
    # def ts():
    #     return int(time.time())

#获得appSecret
    def appSecret(self):
        url = "http://api.admin.adhudong.com/cpaExternal/getCpaEffectKey.htm"
        post_json = {
            'appKey':self.appKey,
            'startTime':self.startTime,
            'endTime':self.endTime,
            'ts':self.ts
        }
        re = requests.get(url=url, params=post_json)
        return re.text

    def appSecret_update(self):
        url = "http://api.admin.adhudong.com/cpaExternal/cpaEffectUpdateKey.htm"
        post_json = {
            'appKey':self.appKey,
            'ts':self.ts
        }
        re = requests.get(url=url, params=post_json)
        # print re.url
        # print re.content
        return re.text

#查询我方接口
    def getDatas(self,appSecret):
        url ="http://api.admin.adhudong.com/cpaExternal/cpaEffect.htm"
        post_json = {
            'appKey':self.appKey,
            'appSecret':appSecret,
            'startTime':self.startTime,
            'endTime':self.endTime,
            'pageNum':self.pageNum,
            'pageSize':self.pageSize,
            'ts':self.ts

        }
        re=requests.get(url=url,params=post_json)
        print re.url
        # print re.content
        # data=json.dumps(re['data'],encoding='utf-8', ensure_ascii=False)
        data = re.json()['data']
        data_len = len(data)
        datas = []
        if data:
            for i in range(data_len):
                data_dict={}
                data_dict["id"]=data[i]['id']
                data_dict["createTime"] = data[i]['createTime'].encode("utf-8")
                if dict(data[i]).has_key('assessValid') :
                    data_dict["assessValid"] = data[i]['assessValid']
                else:
                    data_dict["assessValid"] ="".encode("utf-8")

                if dict(data[i]).has_key('isValid') :
                    data_dict["isValid"] = data[i]['isValid']
                else:
                    data_dict["isValid"] = "".encode("utf-8")

                if dict(data[i]).has_key("confirmRemark"):
                    print type(data[i]['confirmRemark'])
                    data_dict["confirmRemark"] = data[i]['confirmRemark'].encode("utf-8")
                else:
                    data_dict["confirmRemark"] = "".encode("utf-8")
                datas.append(data_dict)

        return str(datas)



    def update_data(self,appSecret,info):
        url = "http://api.admin.adhudong.com/cpaExternal/cpaEffectUpdate.htm"
        # , {"id": 1, "isValid": 1, "confirmRemark": "", "assessValid": 1, "createTime": "2018-11-30 13: 00: 00"}
        # info="""[{"id": 51,"isValid": 3,"confirmRemark": "","assessValid":"3" ,"createTime": "2018-12-06 17:10:06" }, {"id": 52, "isValid": 2, "confirmRemark": "", "assessValid": 1, "createTime": "2018-12-06 17:10:06"}]"""
        post_json = {
            'appKey': self.appKey,
            'appSecret': appSecret,
            'ts': self.ts,
            'array':info,
        }
        re=requests.get(url=url, params=post_json)
        print re.url
        print re.content

if __name__=='__main__':
    cpd = cpaData(appKey='wlq_client1',startTime='2018-12-17 00:00:00',endTime='2018-12-17 23:59:59',pageNum=1)
    appSecret =cpd.appSecret()
    appSecret_update = cpd.appSecret_update()
    # print appSecret
    print cpd.getDatas(appSecret)
    # cpd.update_data(appSecret_update,cpd.getDatas(appSecret))