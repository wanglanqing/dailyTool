# -*- coding: utf-8 -*-
# @Time    : 2018/6/1 18:03
# @Author  : wanglanqing

import datetime
import time
import requests
import random
from hdt_tools.utils.db_info import *

class PreDataBase(object):

    def __init__(self, demand_user='autoadv', demand_pwd='qq123456', admin_user='test', admin_pwd='!Qq123456'):
        self.db = DbOperations()
        self.demand_s = requests.session()
        self.admin_s = requests.session()
        self.demand_url = 'http://api.demand.adhudong.com/api/advert/login.htm?name={0}&password={1}'.format(demand_user, demand_pwd)
        print self.demand_url
        self.admin_url = 'http://api.admin.adhudong.com/login/login_in.htm?name={0}&pwd={1}'.format(admin_user, admin_pwd)
        print self.demand_url
        self.demand_s.get(self.demand_url)
        self.admin_s.get(self.admin_url)

    @staticmethod
    def get_now():
        return str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    @staticmethod
    def get_today(detla=0):
        return (datetime.datetime.now()-datetime.timedelta(days=detla)).strftime('%Y%m%d')
    @staticmethod
    def get_today_with_delimer(detla=0):
        return (datetime.datetime.now()-datetime.timedelta(days=detla)).strftime('%Y-%m-%d')

    @staticmethod
    def get_timedetla(detla=1):
        return (datetime.datetime.now()+datetime.timedelta(days=detla)).strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def get_random_no(bits=0):
        rlen = str(random.random())
        if bits > len(rlen[2:]):
            return '请求的位数过大'
        else:
            bits_tmp = bits + 2
            return rlen[2:bits_tmp]

    def get_keys(self):
        url = 'http://api.demand.adhudong.com/api/voyager/order/list.htm?aid=210'
        result = self.demand_s.get(url)
        print self.demand_s.cookies
        print result.text

    @staticmethod
    def ts():
        # time.time()
        ts=int(round(time.time() * 1000))
        return str(ts)


    def __del__(self):
        self.db.close_db()

if __name__ == '__main__':
    pdb = PreDataBase()
    # print pdb.get_keys()
    # print PreDataBase.ts()
    print PreDataBase.get_today()
    # print PreDataBase.get_random_no(8)
