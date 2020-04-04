import pandas as pd
from sqlalchemy import create_engine
phone = 10000000760
nickName = 9527
# 此处填入服务器连接
engine = create_engine('mysql+pymysql://timing_read_only:db_only_hsyt21@rr-bp12u85w22spt5976do.mysql.rds.aliyuncs.com:3306/timing?charset=utf8')  # 正式服
ID = "1"
Phone = phone
while len(ID) == 1:
    Phone = Phone + 1
    ID = pd.read_sql('SELECT ID FROM t_user where phone="' + str(Phone) + '" ', engine)
print(Phone)
captcha = pd.read_sql('select captcha FROM t_captcha WHERE phone = "' + str(Phone) + '" order by postTime desc', engine)
captcha = captcha.iloc[0, 0]  # 正式服数据库拿验证码
print(captcha)