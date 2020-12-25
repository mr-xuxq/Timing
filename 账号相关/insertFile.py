import pandas as pd
import datetime
from sqlalchemy import create_engine

#engine = create_engine('mysql+pymysql://(用户名):(密码)@(主机名):3306/timing?charset=utf8')
#循环
def timing_offical():
    for phone in range(i,i+2000):
        #从数据库获取ID
        captchaList= pd.read_sql('SELECT ID FROM t_user where phone="' + str(phone) + '" ', engine1)
        #ID长度判别
        if len(captchaList)==0 :
            #填表
            file = open('Timing正式服未注册账号.txt', 'a')
            file.write(str(phone) + '\n')
            file.close()
            print(str(phone))

def timing_test():
    for phone in range(i,i+1000):
        #从数据库获取ID
        captchaList= pd.read_sql('SELECT ID FROM t_user where phone="' + str(phone) + '" ', engine2)
        #ID长度判别
        if len(captchaList)==0 :
            #填表
            file = open('Timing测试服未注册账号.txt', 'a')
            file.write(str(phone) + '\n')
            file.close()
            print(str(phone))

def light_offical():
    for phone in range(i,i+1000):
        #从数据库获取ID
        captchaList= pd.read_sql('SELECT ID FROM t_sp_users where phone="' + str(phone) + '" ', engine3)
        #ID长度判别
        if len(captchaList)==0 :
            #填表
            file = open('猩猩点灯正式服未注册账号.txt', 'a')
            file.write(str(phone) + '\n')
            file.close()
            print(str(phone))


def light_test():
    for phone in range(i,i+1000):
        #从数据库获取ID
        captchaList= pd.read_sql('SELECT ID FROM t_sp_users where phone="' + str(phone) + '" ', engine4)
        #ID长度判别
        if len(captchaList)==0 :
            #填表
            file = open('猩猩点灯测试服未注册账号.txt', 'a')
            file.write(str(phone) + '\n')
            file.close()
            print(str(phone))

#初始时间
print(datetime.datetime.now())
# 赋初始值
i = 10000000001

# 以下为函数调用，如有不需要查找的，可注释掉
timing_offical()
#timing_test()
#light_offical()
#light_test()


# 结束时间
print(datetime.datetime.now())
