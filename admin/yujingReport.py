# -*- coding: utf-8 -*-
# @Time    : 2019/1/24 10:57
# @Author  : wanglanqing

import random
from hdt_tools.utils.db_info import DbOperations


class yuJing(object):
    def __init__(self,dataList):
        self.db = DbOperations()
        self.data = dataList

    def adzoneUp(self):
        for item in self.data:
            sql = """
                INSERT INTO `voyager`.`report_zone` (`date`, `adzone_id`, `media_industry`, `master_id`, `media_id`, `media_level`, `media_manager_id`, `media_operator_id`, `settle_method`, `quality`, `access_type`, `cooperate_type`, `adzone_show_num`, `adzone_show_uv`, `adzone_effect_num`, `adzone_inefficient_num`, `adzone_click_uv`, `lottery_num`, `lottery_uv`, `show_num`, `show_invalid_num`, `show_uv`, `adclick_num`, `adclick_invalid_num`, `adclick_uv`, `adzone_consume`, `platform_income`, `media_income`, `media_income_cash`, `media_cost`, `update_time`, `lottery_xiexie_num`, `lottery_other_num`, `normal_advertisers_num`, `td_advertisers_num`, `zone_effect_num`, `ad_effect_num`, `cpa_consume`, `cpa_media_cost`, `cpa_media_income`, `cpa_media_income_cash`, `ocpa_effect_num`, `ocpa_click_num`, `ocpa_consume`, `ocpa_expect_consume`, `ocpa_media_income`, `ocpa_show_num`) VALUES ( '2019-01-23', '{}', '69', '82', '67', '5', '76', '206', '1', '2', '1', '1', '0', '0', '{}', '11', '16', '117', '16', '79', '32', '15', '20', '8', '8', '796', '130', '666', '546', '6600.00', '2019-01-24 10:32:14', '20', '97', '28', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0');
                INSERT INTO `voyager`.`report_zone` (`date`, `adzone_id`, `media_industry`, `master_id`, `media_id`, `media_level`, `media_manager_id`, `media_operator_id`, `settle_method`, `quality`, `access_type`, `cooperate_type`, `adzone_show_num`, `adzone_show_uv`, `adzone_effect_num`, `adzone_inefficient_num`, `adzone_click_uv`, `lottery_num`, `lottery_uv`, `show_num`, `show_invalid_num`, `show_uv`, `adclick_num`, `adclick_invalid_num`, `adclick_uv`, `adzone_consume`, `platform_income`, `media_income`, `media_income_cash`, `media_cost`, `update_time`, `lottery_xiexie_num`, `lottery_other_num`, `normal_advertisers_num`, `td_advertisers_num`, `zone_effect_num`, `ad_effect_num`, `cpa_consume`, `cpa_media_cost`, `cpa_media_income`, `cpa_media_income_cash`, `ocpa_effect_num`, `ocpa_click_num`, `ocpa_consume`, `ocpa_expect_consume`, `ocpa_media_income`, `ocpa_show_num`) VALUES ('2019-01-24', '{}', '0', '0', '40', '1', '0', '0', '1', NULL, NULL, NULL, '0', '0', '{}', '0', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0.00', '2019-01-24 10:26:17', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0');
                INSERT INTO `voyager`.`report_zone_hour` (`date`, `adzone_id`, `media_industry`, `master_id`, `media_id`, `media_level`, `media_manager_id`, `media_operator_id`, `settle_method`, `quality`, `access_type`, `cooperate_type`, `adzone_show_num`, `adzone_show_uv`, `adzone_effect_num`, `adzone_inefficient_num`, `adzone_click_uv`, `lottery_num`, `lottery_uv`, `show_num`, `show_uv`, `adclick_num`, `adclick_uv`, `adzone_consume`, `platform_income`, `media_income`, `media_income_cash`, `media_cost`, `hour`, `update_time`) VALUES ( '2019-01-23', '{}', '69', '82', '67', '5', '76', '206', '1', '2', '1', '1', '0', '0', '{}', '10', '6', '31', '6', '23', '6', '3', '1', '142', '25', '117', '117', '3600.00', '10', '2019-01-24 10:44:57');
                INSERT INTO `voyager`.`report_zone_hour` (`date`, `adzone_id`, `media_industry`, `master_id`, `media_id`, `media_level`, `media_manager_id`, `media_operator_id`, `settle_method`, `quality`, `access_type`, `cooperate_type`, `adzone_show_num`, `adzone_show_uv`, `adzone_effect_num`, `adzone_inefficient_num`, `adzone_click_uv`, `lottery_num`, `lottery_uv`, `show_num`, `show_uv`, `adclick_num`, `adclick_uv`, `adzone_consume`, `platform_income`, `media_income`, `media_income_cash`, `media_cost`, `hour`, `update_time`) VALUES ('2019-01-24', '{}', '0', '0', '40', '1', '0', '0', '1', NULL, NULL, NULL, '0', '0', '{}', '0', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0.00', '10', '2019-01-24 10:42:57');
                    """.format(item[0],item[1],item[0],item[2],item[0],item[1],item[0],item[2])
            print sql
            sql_list = sql.split(';')
            for tmpsql in sql_list:
                self.db.execute_sql(tmpsql)

if __name__=="__main__":

    def getTodayNum(adzone,pos,max):
        final= []
        zone = int(adzone)+1
        for i in range(adzone,zone):
            tmp = []
            today=random.randint(2000,max)
            chazhi= random.uniform(0.300,0.810)
            if pos ==1:
                chazhi = random.uniform(0.300, 0.810)
            else:
                chazhi = -(random.uniform(0.300, 0.810))
            yestoday = today/(1+chazhi)
            tmp.append(i)
            tmp.append(int(yestoday))
            tmp.append(today)
            final.append(tmp)
        return final
    # print getTodayNum(101,1,10000)

    YJ = yuJing(getTodayNum(372,0,3000))
    YJ.adzoneUp()