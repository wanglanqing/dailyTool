# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 13:37
# @Author  : wanglanqing

import json
from hdt_tools.base.PreDataBase import *

class demandApi(PreDataBase):
    def __init__(self):
        super(demandApi,self).__init__()

    def get_keys(self):
        # url = 'http://api.demand.adhudong.com/api/voyager/order/list.htm?aid=210'
        url = "https://apidemand.adhudong.com/api/voyager/creative/get.htm?cid=1438"
        result = self.demand_s.get(url)
        # print self.demand_s.cookies
        # print result.text
        # print result.json()['data']
        # print str(result.json()['data']['data'][0].keys())[3:-2] .replace(" u'",'').replace("'",'')
        print str(result.json()['data'].keys())[3:-2].replace(" u'", '').replace("'", '')


    def split_url(self):
        # url = "https://apidemand.adhudong.com/api/voyager/order/payment/change.htm?aid=2222455&oids=1608&type=2&value=1000000&unit=1"
        url = "https://apidemand.adhudong.com/api/voyager/order/payment/change.htm"
        if url.__contains__('?'):
            url_list = url.split('?')
            print url_list
            url_f = url_list[0]
            params = "{'" + url_list[1].replace('=',"':'").replace('&',"','") + "'}"
            print url_f, params
        else:
            url_f = url
            params=''
            print url_f, params






if __name__ == '__main__':
    da = demandApi()
    da.get_keys()
    # da.split_url()