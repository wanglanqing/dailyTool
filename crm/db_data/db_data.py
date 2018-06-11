# -*- coding: utf-8 -*-
# @Time    : 2018/6/4 9:29
# @Author  : wanglanqing
import random
import time
from hdt_tools.base.PreDataBase import *


class DbData(PreDataBase):
    def __init__(self):
        super(DbData, self).__init__()
        self.now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.random_no = str(random.random())
        self.detla = (datetime.datetime.now() - datetime.timedelta(days=20)).strftime('%Y-%m-%d %H:%M:%S')


    def crm_delivery_log(self):
        '''crm_delivery_log'''
        for i in range(0,1):
            sql = """INSERT INTO crm_delivery_log (agent_id, customer_id, order_id, logistic_tag, deliverystatus, deliveryMsg, create_time) VALUES
    ('2222457', '2222458', '16', '3926585603491', '3', '{\"status\":\"0\",\"msg\":\"ok\",\"result\":{\"number\":\"3926585603493\",\"type\":\"yunda\",\"list\":[{\"time\":\"2018-03-12 13:07:31\",\"status\":\"beijing\"},{\"time\":\"2018-03-11 20:26:18\",\"status\":\"tele:18714266261\"},{\"time\":\"2018-03-10 10:29:52\",\"status\":\"coma\"},{\"time\":\"2018-03-10 10:11:40\",\"status\":\"saca\"},{\"time\":\"2018-03-09 01:43:56\",\"status\":\"sddd\"},{\"time\":\"2018-03-08 21:21:10\",\"status\":\"guang\"},{\"time\":\"2018-03-08 21:01:24\",\"status\":\"dong\"},{\"time\":\"2018-03-08 17:26:51\",\"status\":\"ss\"}],\"deliverystatus\":\"3\",\"issign\":\"1\"}}',
    '""" + super(DbData, self).get_now()  + """');"""
            # print sql
            self.db.execute_sql(sql)

    def crm_sms_log(self):
        '''crm_sms_log'''
        for i in range(0,10):

            sql = """INSERT INTO crm_sms_log (agent_id, customer_id, send_time, phone, order_no, type, state, call_sid, content, create_time) VALUES
('2222457', '2222458', '{0}', '13621236449', '1235469', '2', '0', '18052912jkd1', 'smscontent 13214521144', '{1}');""".format(self.now, self.now)
            # print sql
            time.sleep(3)
            self.db.execute_sql(sql)

    def crm_order(self):
        '''crm_order'''
        for i in range(0,7):
            rdn = str(random.random())[3:]
            time.sleep(1)
            sql = """
            INSERT INTO voyager.crm_order (agent_id, customer_id, order_no, product_id, product_ext_id, product_name, price, sale_price, product_num, payment_mode, status, state, ad_order_id, order_url, ad_click_tag, channel, tag, user_cookie, ip, except, buyer_name, buyer_province, buyer_city, buyer_county, buyer_address, buyer_phone, buyer_comment, logistic_id, logistic_tag, logistic_state, seller_remark, sender, sender_phone, send_time, order_time, update_time) VALUES
('2222457', '2222458', '{0}', '6', '6', 'wlq产品1', '10001', '9999', '1', '1', '1', '{1}', NULL, NULL, NULL, NULL, NULL, 'ddd', '172.168.14.145', '-1', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '1', '3926585603493 ', '1', NULL, NULL, NULL, NULL, '{2}', '{3}');
            """.format(rdn, i, self.now, self.now)
            self.db.execute_sql(sql)

if __name__ == '__main__':
    dd = DbData()
    # dd.crm_sms_log()
    dd.crm_delivery_log()
    # dd.crm_order()
