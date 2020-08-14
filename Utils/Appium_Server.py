'''
Created on 2019年12月2日

@author: likecan
'''
#coding:utf-8
import os,threading,sys
sys.path.append('./')
from Utils.Adb_Order import adb_order
from Utils.Device_Config import device_config

class appium_server(object):
    '''
    classdocs
    '''


    def __init__(self):
        self.device_infor = device_config()
        self.device_name_list = adb_order().get_device_name()

        
    def create_command_list(self):
        '''
        根据设备数量，启动appium服务
        '''
        appium_server_order = []
        port = 4723
        boot_port = port + 1
        for device_name in self.device_name_list:
            self.device_infor.set_device_infor_to_config(device_name, boot_port, port)#将设备信息和对应的串口号写入到本地文件中
            command = 'appium -p {0} -bp {1} -U {2} --no-reset --session-override'.format(str(port),str(boot_port),device_name)#另起线程执行
            appium_server_order.append(command)
            port = boot_port + 1
            boot_port = port + 1
        return appium_server_order
    
    def start_appium_server(self,command):
        os.popen(command,'w')
        
    def kill_server(self):
        '''
        杀掉当前所有的node.exe进程
        '''
        find_node = os.popen('tasklist | findstr "node.exe"').readlines()
        print(find_node)
        if len(find_node) > 0:
            print('kill')
            os.system('taskkill -F -PID "node.exe"')
    
    def main(self):
        self.kill_server()
        self.device_infor.clear_device_infor_config()
        command_list = self.create_command_list()
        thread = []
        for command in command_list:
            print(command)
            t = threading.Thread(target=self.start_appium_server,args = (command,))
            thread.append(t)
        for t in thread:
            t.run()

a_server = appium_server()
a_server.main()
            
