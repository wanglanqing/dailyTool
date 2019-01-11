# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 13:37
# @Author  : wanglanqing

import json
import string
from hdt_tools.base.PreDataBase import *

class demandApi(PreDataBase):
    def __init__(self):
        super(demandApi,self).__init__()

    def get_keys(self,url):
        # url = 'http://api.demand.adhudong.com/api/voyager/order/list.htm?aid=210'
        # url = "https://apidemand.adhudong.com/api/agent/customer/summary/list.htm?current=1&search=&pageSize=10&level="
        result = self.demand_s.get(url)
        # print self.demand_s.cookies
        # print result.text
        # print result.text
        # .json()['data']
        print str(result.json()['data'].keys())[2:-1].replace(" u'",'').replace("'",'')
        # print str(result.json()['data']['data'][0].keys())[3:-2] .replace(" u'",'').replace("'",'')
        # print str(result.json()['data'].keys())[3:-2].replace(" u'", '').replace("'", '')


    def split_url(self):
        # url = "https://apidemand.adhudong.com/api/voyager/order/payment/change.htm?aid=2222455&oids=1608&type=2&value=1000000&unit=1"
        url = "https://apidemand.adhudong.com/api/voyager/advertiser/getInfo.htm?id=2222229"
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



def ad_show():
    param={'pids':1,'uniq_tag':'11asdsd','ip':'172.16.144.19 ','cookie':'1sadsd222111','device':'IOS','adzone_id':1610,'pos_num':'1_0','act_id':243}
    param['cookie']=''.join(random.sample(string.ascii_letters+string.hexdigits,8))
    url = "http://172.16.105.11:17091/ad_bidding.do"
    re=requests.get(url,params=param)

    print type(re.json())
    print type(re.text)


if __name__ == '__main__':
    da = demandApi()
    da.get_keys('https://apidemand.adhudong.com/api/crm/summary.htm?aid=2222456')
    # ad_show()
    # da.split_url()