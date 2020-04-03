import subprocess
import os
class Get:

    devicesinfo = str(subprocess.check_output("adb devices")).split("\\r\\n")
    # print(devicesinfo)
    consult = devicesinfo[1].split("\\t")
    if devicesinfo[1] == '':
        print('连接失败')
    else:
        # 获得连接手机的设备号
        print("当前手机设备号:" + consult[0])
    # 获得连接手机的版本号
    platformV = os.popen('adb shell getprop ro.build.version.release').read()
    print("当前手机版本号：" + platformV)
    deviceN = consult[0]
    result = [platformV, deviceN]
