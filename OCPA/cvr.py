# -*- coding: utf-8 -*-
# @Time    : 2018/10/12 15:36
# @Author  : wanglanqing

from hdt_tools.base.PreDataBase import *


class CVR(PreDataBase):
    def __init__(self,days, adv_id=None, adzone_id=None, ad_id=None, url=None):
        super(CVR,self).__init__()
        self.d1_fator = 0.5
        self.d2_fator = 0.25
        self.d3_fator = 0.25
        self.adv_id = adv_id
        self.ad_id = ad_id
        self.adzone_id = adzone_id
        self.url = url
        self.days=days
        pass

    def caculate_cvr(self):
        dc={}
        tmp=0

        # 查询近3天的记录
        for i in range(0,self.days):
            print '============='
            cvr_final = 0.0
            #查询当天日期
            d = PreDataBase.get_today(i)
            dd = PreDataBase.get_today_with_delimer(i)
            show_sql= """select count(*) from voyagerlog.ad_show_log{} where status=1""".format(d)
            click_sql= """select count(*) from voyagerlog.ad_click_log{} where status=1""".format(d)
            effect_sql= """select count(*) from voyagerlog.ad_effect_log_{}""".format(d[4:6])

            #1.广告位  + 广告订单 +创意url
            if self.ad_id and self.adzone_id and self.url is not None:
                #查询展现数量
                # sql = """select count(*) from voyagerlog.ad_show_log{}
                #         where ad_order_id={}
                #         and adzone_id={}
                #         and url='{}'""".format(d, self.ad_id, self.adzone_id, self.url)
                show_sql=show_sql + """ and ad_order_id={} and adzone_id={} and url='{}'""".format(self.ad_id, self.adzone_id, self.url)
                click_sql=click_sql + """ and ad_order_id={} and adzone_id={} and url like '%{}%'""".format(self.ad_id, self.adzone_id, self.url.split('=')[0])
                effect_sql=effect_sql + """ where ad_order_id={} and adzone_id={} and url='{}'
                                and create_time>='{} 00:00:00'
                                and create_time<='{} 23:59:59'""".format(self.ad_id,self.adzone_id,self.url,dd,dd)

            #2.广告位 + 创意url
            elif self.adzone_id and self.url is not None:
                # 查询展现数量
                # sql = """select count(*) from voyagerlog.ad_show_log{}
                #         where adzone_id={}
                #         and url='{}'""".format(d, self.adzone_id, self.url)
                show_sql = show_sql + """ and adzone_id={} and url='{}'""".format(self.adzone_id,self.url)
                click_sql = click_sql + """ and  adzone_id={} and url like '%{}%'""".format(self.adzone_id, self.url.split('=')[0])
                effect_sql = effect_sql + """ where  adzone_id={} and url='{}'
                                and create_time>='{} 00:00:00' and create_time<='{} 23:59:59'""".format(self.adzone_id, self.url, dd, dd)

            # 3.广告位 + 广告订单
            elif self.adzone_id and self.ad_id is not None:
                show_sql = show_sql + """ and ad_order_id={} and adzone_id={}""".format(self.ad_id,self.adzone_id)
                click_sql = click_sql + """ and ad_order_id={} and adzone_id={}""".format(self.ad_id,self.adzone_id)
                effect_sql = effect_sql + """ where ad_order_id={} and adzone_id={}
                                and create_time>='{} 00:00:00' and create_time<='{} 23:59:59'""".format(self.ad_id, self.adzone_id, dd, dd)

            #4.广告位
            elif self.adzone_id is not None:
                show_sql = show_sql + """ and adzone_id={}""".format(self.adzone_id)
                click_sql = click_sql + """ and  adzone_id={}""".format(self.adzone_id)
                effect_sql = effect_sql + """ where  adzone_id={} and create_time>='{} 00:00:00' and create_time<='{} 23:59:59'""".format(self.adzone_id, dd, dd)

            # 5. 广告订单
            elif  self.ad_id is not None:
                show_sql = show_sql + """ and ad_order_id={}""".format(self.ad_id)
                click_sql = click_sql + """ and ad_order_id={}""".format(self.ad_id)
                effect_sql = effect_sql + """ where ad_order_id={} and create_time>='{} 00:00:00' and create_time<='{} 23:59:59'""".format(self.ad_id, dd, dd)

            # 6. 广告主
            elif self.adv_id is not None:
                show_sql = show_sql + """ and advertiser_id={}""".format(self.adv_id)
                click_sql = click_sql + """ and advertiser_id={}""".format(self.adv_id)
                effect_sql = effect_sql + """ where advertiser_id={} and create_time>='{} 00:00:00' and create_time<='{} 23:59:59'""".format(
                    self.adv_id, dd, dd)
            # 7.系统平均
            else:
                show_sql = show_sql
                click_sql = click_sql
                effect_sql = effect_sql
                effect_sql = effect_sql + """ where create_time>='{} 00:00:00'
                    and create_time<='{} 23:59:59'""".format(dd, dd)

            # total=int(self.db.execute_sql(sql)[0][0])
            total=int(self.db.execute_sql(show_sql)[0][0])
            print d + '的展现个数是:',total
            #大于1000次展现的数据，计算每天的CVR
            # if total>=1000:
            # 计算效果数
            # sql_effect_num = """select count(*) from voyagerlog.ad_effect_log_10 where ad_order_id={}
            #                 and adzone_id={}
            #                 and url='{}'
            #                 and create_time>='{} 00:00:00'
            #                 and create_time<='{} 23:59:59'""".format(self.ad_id,self.adzone_id,self.url,dd,dd)
            # effect_num =int(self.db.execute_sql(sql_effect_num)[0][0])
            effect_num = int(self.db.execute_sql(effect_sql)[0][0])
            print d+'的效果个数是:',effect_num

            #查询广告点击数
            # sql_click_num = """select count(*) from voyagerlog.ad_click_log{}
            #             where ad_order_id={}
            #             and adzone_id={}
            #             and url like '%{}%'""".format(d, self.ad_id, self.adzone_id, self.url.split('=')[0])
            # click_num = int(self.db.execute_sql(sql_click_num)[0][0])
            click_num = int(self.db.execute_sql(click_sql)[0][0])
            print d+'的点击个数是:',click_num


            if click_num>0:
                cvr = float(effect_num)/click_num
                cvr_tmp=0.0
                if i==0:
                    print d+'的cvr是:',cvr, ',加权值：',cvr * 0.5
                    cvr_final=cvr_final+cvr*0.5
                else:
                    print d + '的cvr是:',cvr, ',加权值：',cvr * 0.25
                    cvr_final=cvr_final+cvr*0.25
            else:
                print '点击个数为0，无法计算cvr'
            # else:
            #     print d + '展现量小于1000，不查询效果数和点击数'
        if cvr_final>0.1:
            print 'CVR超过10%，按10%计算。 值为',cvr_final
        else:
            print cvr_final

    def modifyUrl(self):
        url = "https://display.adhudong.com/new/ad/vipjr.html?utm_click=${click_tag}"
        for i in range(0,1000):
            print url.replace('display',str(i)+'display')

    @staticmethod
    def testmy():
        mylist=[]
        for i in range(0,4):
            mylist.append(i)
        print mylist

if __name__=='__main__':
    # c = CVR(3, adv_id=2361,adzone_id=1822,ad_id=1635,url='https://display.adhudong.com/new/ad/vipjr.html?utm_click=${click_tag}')
    # c = CVR(3, adv_id=2222231, adzone_id=1823, ad_id=1636,url='https://display.adhudong.com/new/ad/vipjr.html?utm_click=${click_tag}')
    # c = CVR(3, adv_id=2222234, adzone_id=1824, ad_id=1637,url='https://display.adhudong.com/new/ad/vipjr.html?utm_click=${click_tag}')
    # c = CVR(3, adv_id=2222238, adzone_id=1825, ad_id=1579,url='https://display.adhudong.com/new/ad/vipjr.html?utm_click=${click_tag}')
    # c = CVR(3, adv_id=2222247, adzone_id=1826, ad_id=1578,url='https://display.adhudong.com/new/ad/vipjr.html?utm_click=${click_tag}')
    # c = CVR(3, adv_id=2222502, adzone_id=1827, ad_id=1639,url='https://display.adhudong.com/new/ad/vipjr.html?utm_click=${click_tag}')
    # c = CVR(3, adv_id=2222263, adzone_id=1828, url='https://display.adhudong.com/new/ad/vipjr.html?utm_click=${click_tag}')
    # c = CVR(3, adv_id=2222263, adzone_id=1823, ad_id=1636)
    c = CVR(3,ad_id=1641)
    # c = CVR()
    c.caculate_cvr()
    # c.modifyUrl()
    # CVR.testmy()
