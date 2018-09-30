# -*- coding: utf-8 -*-
# @Time    : 2018/6/25 15:01
# @Author  : wanglanqing
from hdt_tools.base.PreDataBase import *
import datetime
from openpyxl import Workbook

class admin_db_data(PreDataBase):
    def __init__(self):
        super(admin_db_data, self).__init__()
        self.now = datetime.datetime.now().strftime('%Y-%m-%d')
        self.detla = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')

    # def del_old_data(self):
    #     sql = "delete from "
    # def report_zone(self):
    def get_actInfo(self):
        key_path=[
            'buddha_question.html',
            'sharp_lottery',
            'draw_card',
            'rotary_table',
            'turntable.html',
            'smash_egg',
            'new_lottery_machine',
            'dice.html',
            'popodino.html',
            'jigsaw.html',
            'card_up.html',
            'lottery_machine',
            'octopus.html',
            'cardloop',
            'doraemon.html',
            'draw_cuts',
            'football.html',
            'earth_day.html',
            'dragonboat.html',
            'whack_mole.html',
            'lottery_claw',
            'nineBlockBox.html',
            'redpack_rain',
            'scratch_card',
            'gashapon'
        ]
        kpl = len(key_path)
        re_list = []
        for i in range(kpl):
            sql = '''
                    SELECT
                    a.id as '活动id',a.act_name  as '活动名称', t.id as '模板id',t.template_name AS '模板名称',
                    v.location_adress
                FROM
                    base_act_info a
                INNER JOIN base_template_info t ON a.template_id = t.id
                LEFT JOIN template_type v ON t.template_type_id = v.id
                WHERE
                    v.location_adress like '%/new/{}%'
                ORDER BY
                    v.location_adress DESC
                LIMIT 0,100;
                    '''.format(key_path[i])
            re= self.db.execute_sql(sql)
            re_len = len(re)
            if re_len>0:
                for i in range(re_len):
                    re_list.append(re[i])
        return re_list

    def save_result(self,result):
        wb = Workbook()
        ws =wb.active
        row = len(result)
        for i in range(row):
            ws.append(result[i])
        wb.save('result.xls')



if __name__=='__main__':
    add = admin_db_data()
    add.save_result(add.get_actInfo())