# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 13:37
# @Author  : wanglanqing

import json
from hdt_tools.base.PreDataBase import *

class demandApi(PreDataBase):
    def __init__(self):
        super(demandApi,self).__init__()

    def get_keys(self):
        url = 'http://api.demand.adhudong.com/api/voyager/order/list.htm?aid=210'
        result = self.demand_s.get(url)
        # print self.demand_s.cookies
        # print result.text
        print result.json()['data']['data'][0].keys()


if __name__ == '__main__':
    da = demandApi()
    da.get_keys()