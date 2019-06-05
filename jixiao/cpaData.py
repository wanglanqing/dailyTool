# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 17:38
# @Author  : wanglanqing

import datetime,time,json
import requests
import urlparse

class cpaData(object):
    def __init__(self,appKey=None,startTime=None,endTime=None,pageNum=None,pageSize=20,planID=None,mediaId=None,adzoneId=None):
        self.appKey=appKey
        self.startTime=startTime
        self.endTime=endTime
        self.pageNum=pageNum
        self.pageSize=pageSize
        self.ts = int(time.time())
        self.planId = planID
        self.mediaId = mediaId
        self.adzoneId = adzoneId

#获得当前时间，转换为时间戳
    # @staticmethod
    # def ts():
    #     return int(time.time())

#获得appSecret
    def appSecret(self):
        url = "http://api.admin.adhudong.com/cpaExternal/getCpaEffectKey.htm"

        post_json = {
            'appKey': self.appKey,
            'startTime': self.startTime,
            'endTime': self.endTime,
            'ts': self.ts
        }
        if self.planId:
            post_json['planId'] = self.planId
        if self.mediaId:
            post_json['mediaId'] = self.mediaId
        if self.adzoneId:
            post_json['adzoneId'] = self.adzoneId
        print post_json
        re = requests.get(url=url, params=post_json)
        # print re.text
        print re.url
        return re.text

    def appSecret_update(self):
        url = "http://api.admin.adhudong.com/cpaExternal/cpaEffectUpdateKey.htm"
        post_json = {
            'appKey':self.appKey,
            'ts':self.ts,
            # 'startTime':self.startTime,
            # 'endTime':self.endTime
        }
        re = requests.get(url=url, params=post_json)
        print re.url
        # print re.content
        return re.text

#查询我方接口
    def getDatas(self,appSecret):
        '''
        :param appSecret:
        mediaId
        adzoneId
        :return:
        '''
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
        if self.planId:
            post_json['planId'] = self.planId
        if self.mediaId:
            post_json['mediaId'] = self.mediaId
        if self.adzoneId:
            post_json['adzoneId'] = self.adzoneId
        re=requests.get(url=url,params=post_json)
        print 'get url is :'
        print urlparse.unquote((re.url).decode("utf-8"))
        # print re.content
        # data=json.dumps(re['data'],encoding='utf-8', ensure_ascii=False)
        data = re.json()['data']
        datas = []
        if data:
            data_len = len(data)
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
                    # print type(data[i]['confirmRemark'])
                    data_dict["confirmRemark"] = data[i]['confirmRemark'].encode("utf-8")
                else:
                    data_dict["confirmRemark"] = "".encode("utf-8")

                if dict(data[i]).has_key('planId'):
                    data_dict["planId"] = data[i]['planId']
                else:
                    data_dict["planId"] = "".encode("utf-8")

                if dict(data[i]).has_key('mediaId'):
                    data_dict["mediaId"] = data[i]['mediaId']
                else:
                    data_dict["mediaId"] = "".encode("utf-8")
                datas.append(data_dict)

                if dict(data[i]).has_key('adzoneId'):
                    data_dict["adzoneId"] = data[i]['adzoneId']
                else:
                    data_dict["adzoneId"] = "".encode("utf-8")
        # return len(datas)
        return str(datas)



    def update_data(self,appSecret,info=None):
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


    def update_data_new(self,appSecret=None,info=None):
        url = "http://api.admin.adhudong.com/cpaExternal/cpaEffectUpdateNew.htm"
        post_json = {
            'planId': self.planId,
            'appKey': self.appKey,
            'appSecret': appSecret,
            'ts': self.ts,
            'array':info,
            'adzoneId':self.adzoneId,
            # 'mediaId':self.mediaId
        }
        re=requests.get(url=url, params=post_json)
        print urlparse.unquote((re.url).decode("utf-8"))
        print re.content

if __name__=='__main__':
    #
    cpd = cpaData(appKey='adv-kaishen',startTime = '2019-05-14 15:42:00', endTime = '2019-05-14 16:12:00')
    appSecret=cpd.appSecret()
    # appSecret=cpd.appSecret_update()
    re= cpd.getDatas(appSecret)
    print re
    # '考核确认 1-有效  2-无效 3-待定',
    info = '[{"date":"2018-12-28",' \
           '"assValidNum":1,"assInvalidNum":1,"assDeterNum":0,"type":2}]'
    # print cpd.update_data_new(appSecret, info)


    # cpd.update_data(appSecret_update,cpd.getDatas(appSecret))