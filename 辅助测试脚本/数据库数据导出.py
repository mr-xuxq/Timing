import pandas as pd
import datetime
from sqlalchemy import create_engine

#engine = create_engine('mysql+pymysql://(用户名):(密码)@(主机名):3306/timing?charset=utf8')

class OutputData():

    def getAndroidNumber(self):
        # 从数据库获取ID(从active_record表内获取这一天后所有使用Android登录的用户的信息)
        captchaList = pd.read_sql('SELECT DISTINCT(userID),brand,phoneModel,os,postTime FROM t_active_record WHERE postTime > "2020-12-25 00:00:00" AND market <> "appstore" order by postTime desc ', engine2)
        file = open('Android数据.xlsx', 'w')
        file.write(str(captchaList) + '\n')
        file.close()

if __name__ == '__main__':
    OutputData().getAndroidNumber()