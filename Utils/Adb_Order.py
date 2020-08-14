'''
Created on 2019年10月14日

@author: likecan
'''
#coding=utf-8

import re
from os import popen,system
class adb_order():


    
    def get_current_package_and_activity(self):
        '''
        获取当前打开的应用的包名和类名
        '''
        adb_print = popen('adb shell dumpsys window | findstr mCurrentFocus')
        adb_print_str = adb_print.read()
        print(adb_print_str)
        return adb_print_str.split(' ')[4][:-2].split('/')
    
    def get_device_name(self):
        '''
        获取设备串号
        '''
        adb_device = popen('adb devices')
        adb_device_print = adb_device.read()
        device_name_list = []
        if adb_device_print.count('device') > 1:
            re_str = r'.*\t'
            re_find = re.findall(re_str, adb_device_print)
            if re_find:
                for i in range(len(re_find)):
                    device_name_list.append(re_find[i][:-1])
        return device_name_list
                    
    
    def cmd_command(self,command):
        system(command)
        
        
    def check_port_is_used(self,port):
        '''
        判断给定的端口是否被使用
        '''
        port_check = popen('netstat -ano | findstr %s'%str(port)).readlines()
        if len(port_check) > 0:
            return True
        else:
            return False
        
# adb_ord = adb_order()
# print(adb_ord.get_current_package_and_activity())
# adb_ord.cmd_command("adb shell am instrument -w -r    -e debug false -e class 'com.uiautomator2.Simple_U2_Script#open_Face_Entery_Page' com.uiautomator2.test/androidx.test.runner.AndroidJUnitRunner")
