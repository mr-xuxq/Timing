import pandas as pd
import datetime
from sqlalchemy import create_engine

#engine = create_engine('mysql+pymysql://(用户名):(密码)@(主机名):3306/timing?charset=utf8')

class OutputData():

    def getAndroidNumber(self):
        # 从数据库获取ID
        captchaList = pd.read_sql('SELECT DISTINCT(userID),brand,phoneModel,os FROM t_active_record WHERE postTime > ''2020-10-07 20:00:00' AND market <> "appstore"', engine2)
        file = open('Android数据.xlsx', 'a')
        file.write(str(captchaList) + '\n')
        file.close()

if __name__ == '__main__':
    OutputData().getAndroidNumber()